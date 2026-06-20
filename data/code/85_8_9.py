import datetime

def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def date_difference_in_weeks(date1_str, date2_str):
    if not (validate_date(date1_str) and validate_date(date2_str)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
    time_difference = abs((date1 - date2).days)
    difference_in_weeks = round(time_difference / 7, 2)
    return difference_in_weeks

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-29"
    result = date_difference_in_weeks(date1, date2)
    print(result)