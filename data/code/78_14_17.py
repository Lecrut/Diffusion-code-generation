from dateutil.relativedelta import relativedelta

def months_between_dates(date_str1, date_str2):
    from datetime import datetime
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    delta = relativedelta(date2, date1)
    return abs(delta.years * 12 + delta.months)

if __name__ == '__main__':
    print(months_between_dates('2022-01-01', '2023-04-15'))