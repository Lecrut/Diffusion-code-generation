from datetime import datetime

def convert_date(date_str):
    dt = datetime.strptime(date_str, '%m/%d/%Y')
    return dt.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(convert_date('12/31/2023'))
    print(convert_date('01/01/2000'))
    print(convert_date('07/04/1776'))