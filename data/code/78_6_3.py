import calendar

def months_between_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    
    start_date = calendar.datetime(year1, month1, day1)
    end_date = calendar.datetime(year2, month2, day2)
    
    difference = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    return difference

if __name__ == '__main__':
    date_str1 = '2020-01-01'
    date_str2 = '2023-04-15'
    print(months_between_dates(date_str1, date_str2))