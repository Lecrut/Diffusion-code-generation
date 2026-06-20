from datetime import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
    except ValueError:
        date_format = "%d/%m/%Y"
        try:
            date1 = datetime.strptime(date_str1, date_format)
            date2 = datetime.strptime(date_str2, date_format)
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD or DD/MM/YYYY.")
    
    delta = abs((date2 - date1).days)
    return delta

if __name__ == '__main__':
    print(calculate_date_difference('2023-04-01', '2023-04-15'))
    print(calculate_date_difference('01/04/2023', '15/04/2023'))