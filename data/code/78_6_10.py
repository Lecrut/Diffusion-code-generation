import calendar

MONTH_TO_INDEX = {month: i for i, month in enumerate(calendar.month_name[1:])}

def months_between_dates(date_str1, date_str2):
    year1, month1, _ = map(int, date_str1.split('-'))
    year2, month2, _ = map(int, date_str2.split('-'))
    difference = (year2 - year1) * 12 + (month2 - month1)
    return difference

if __name__ == '__main__':
    date_str1 = '2020-01-01'
    date_str2 = '2023-04-15'
    result = months_between_dates(date_str1, date_str2)
    print(result)