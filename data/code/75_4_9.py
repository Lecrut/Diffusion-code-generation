from datetime import datetime

def days_difference(date_str1, date_str2):
    format1 = "%m/%d/%Y"
    format2 = "%Y-%m-%d"
    
    try:
        date1 = datetime.strptime(date_str1, format1)
    except ValueError:
        try:
            date1 = datetime.strptime(date_str1, format2)
        except ValueError:
            raise ValueError("Date format not recognized. Please use 'MM/DD/YYYY' or 'YYYY-MM-DD'.")
    
    try:
        date2 = datetime.strptime(date_str2, format1)
    except ValueError:
        try:
            date2 = datetime.strptime(date_str2, format2)
        except ValueError:
            raise ValueError("Date format not recognized. Please use 'MM/DD/YYYY' or 'YYYY-MM-DD'.")
    
    return abs((date2 - date1).days)

if __name__ == '__main__':
    print(days_difference('01/01/2020', '2020-01-02'))