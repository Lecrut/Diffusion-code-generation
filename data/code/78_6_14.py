import calendar
from datetime import datetime

def months_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    year_diff = date2.year - date1.year
    month_diff = date2.month - date1.month
    
    return (year_diff * 12) + month_diff

if __name__ == '__main__':
    print(months_difference('2023-01-01', '2024-02-01'))