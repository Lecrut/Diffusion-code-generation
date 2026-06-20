from datetime import datetime

MONTHS_PER_YEAR = 12
DAYS_PER_MONTH = 30

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    
    if date2.day < date1.day:
        month_diff -= 1
    
    total_months = (year_diff * MONTHS_PER_YEAR) + month_diff
    return abs(total_months)

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2023-02-15"))