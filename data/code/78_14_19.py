from datetime import datetime

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    day_diff = date2.day - date1.day
    
    months_passed = (year_diff * 12) + month_diff
    
    if day_diff < 0:
        months_passed -= 1
    
    return abs(months_passed)

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2023-02-15"))
    print(months_between_dates("2022-12-31", "2023-01-01"))
    print(months_between_dates("2021-06-15", "2022-07-15"))