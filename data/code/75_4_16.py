import datetime

def calculate_days_difference(date1_str, date2_str):
    date_formats = ['%Y-%m-%d', '%m/%d/%Y']
    
    for format in date_formats:
        try:
            date1 = datetime.datetime.strptime(date1_str, format)
            date2 = datetime.datetime.strptime(date2_str, format)
            break
        except ValueError:
            continue
    
    else:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD or MM/DD/YYYY.")
    
    if date1 == date2:
        return 0
    
    difference = abs((date2 - date1).days)
    return difference

if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "12/31/2022"
    result = calculate_days_difference(date1_str, date2_str)
    print(result)