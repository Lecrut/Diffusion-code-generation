from datetime import datetime

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    if date1 > date2:
        date1, date2 = date2, date1
    
    delta_years = date2.year - date1.year
    delta_months = date2.month - date1.month
    months_passed = (delta_years * 12) + delta_months
    
    if date2.day < date1.day:
        months_passed -= 1
    
    return abs(months_passed)

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2023-02-15"))
    print(months_between_dates("2022-12-31", "2023-01-01"))
    print(months_between_dates("2021-06-15", "2022-07-15"))