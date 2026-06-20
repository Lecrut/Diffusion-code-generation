from datetime import datetime

def days_difference(date_str1, date_str2):
    format1 = "%m/%d/%Y"
    format2 = "%Y-%m-%d"
    
    try:
        date1 = datetime.strptime(date_str1, format1)
    except ValueError:
        date1 = datetime.strptime(date_str1, format2)
    
    try:
        date2 = datetime.strptime(date_str2, format1)
    except ValueError:
        date2 = datetime.strptime(date_str2, format2)
    
    return abs((date1 - date2).days)

if __name__ == '__main__':
    print(days_difference('01/01/2020', '2020-01-02'))