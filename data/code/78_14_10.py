from datetime import datetime

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    if date1 > date2:
        date1, date2 = date2, date1
    
    months = (date2.year - date1.year) * 12 + date2.month - date1.month
    if date2.day < date1.day:
        months -= 1
    
    return abs(months)

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2023-02-15"))