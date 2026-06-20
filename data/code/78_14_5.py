from datetime import datetime

def months_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    delta_years = date2.year - date1.year
    delta_months = date2.month - date1.month
    
    if date2.day < date1.day:
        delta_months -= 1
    
    total_months = (delta_years * 12) + delta_months
    return abs(total_months)

if __name__ == '__main__':
    print(months_between_dates("2022-01-01", "2023-02-15"))