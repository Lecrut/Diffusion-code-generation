import datetime

def calculate_days_difference(date1_str, date2_str):
    date_formats = ['%m/%d/%Y', '%Y-%m-%d']
    
    for date_format in date_formats:
        try:
            date1 = datetime.datetime.strptime(date1_str, date_format)
            date2 = datetime.datetime.strptime(date2_str, date_format)
            break
        except ValueError:
            continue
    else:
        return "Error: Invalid date format. Please use MM/DD/YYYY or YYYY-MM-DD."
    
    if date1 == date2:
        return 0
    
    difference = abs((date2 - date1).days)
    return difference

if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "07/31/2024"
    result = calculate_days_difference(date1, date2)
    print(result)