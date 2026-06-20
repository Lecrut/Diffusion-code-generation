from datetime import datetime

def days_between_dates(date_str1, date_str2):
    try:
        dt1 = datetime.strptime(date_str1, '%Y-%m-%d')
        dt2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return abs((dt2 - dt1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2023-01-15'
    print(days_between_dates(date1, date2))
    
    date3 = '2024-06-01'
    date4 = '2024-06-01'
    print(days_between_dates(date3, date4))
    
    date5 = '2023-12-25'
    date6 = '2024-01-01'
    print(days_between_dates(date5, date6))