import requests
import pandas as pd
import time

def main():
    try:
        url = 'https://rate.bot.com.tw/xrt/flcsv/0/day' # 台湾银行汇率表csv文件
        resp = requests.get(url)
        resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
        data = resp.text.split('\n') # 字符串转列表, 以换行符作分隔

        col_1 = []
        col_2 = []
        col_3 = []
        col_4 = []
        col_5 = []
        for index in range(len(data)): # 通过索引遍历
            if index == 0: continue # 第1行为栏目略过
        
            row = data[index].split(',') # 获取每个值, 字符串转列表, 以逗号作分隔
            for k in range(len(row)):
                if row[k] != '':
                    if k == 0: col_1.append(row[k]) # 币别
                    if k == 2: col_2.append(row[k]) # 现金汇率(本行买入)
                    if k == 12: col_3.append(row[k]) # 现金汇率(卖出)
                    if k == 3: col_4.append(row[k]) # 即期汇率(买入)
                    if k == 13: col_5.append(row[k]) # 即期汇率(卖出)

        headers  = ['币别', '现金银行买入', '现金银行卖出', '即期银行买入', '即期银行卖出']
        export_data = {} # 组装数据, 类型为字典
        export_data[headers[0]] = col_1
        export_data[headers[1]] = col_2
        export_data[headers[2]] = col_3
        export_data[headers[3]] = col_4
        export_data[headers[4]] = col_5
        df = pd.DataFrame(export_data)
        filename = 'exchange_rage_' + time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.csv' # 导出文件名
        df.to_csv(filename, index=False, header=True, encoding='utf-8-sig') # utf-8-sig 解决csv乱码
        print('导出csv成功')
    except:
        print('导出csv失败')

if __name__ == '__main__': # 主入口
    main()