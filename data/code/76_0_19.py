import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_days(date1_str, date2_str):
    if not (validate_date(date1_str) and validate_date(date2_str)):
        return "Error: Invalid date format. Please use YYYY-MM-DD."
    
    date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
    date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
    
    if date1 > date2:
        difference = abs(date1 - date2)
    else:
        difference = date2 - date1
    
    return difference.days

if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-03-20"
    result = calculate_days(date1_input, date2_input)
    print(result)