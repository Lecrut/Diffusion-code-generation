import datetime

def validate_date_format(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_weekday(date_string):
    if not validate_date_format(date_string):
        return "Invalid date format"
    
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    return date_obj.weekday() < 5

if __name__ == '__main__':
    date1 = "2023-10-25"
    date2 = "2023-10-26"
    date3 = "2023-10-27"
    date4 = "2023-10-28"
    date5 = "2023-10-29"
    invalid_date = "2023/10/25"
    
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")
    print(f"Is {date5} a weekday? {is_weekday(date5)}")
    print(f"Is {invalid_date} a weekday? {is_weekday(invalid_date)}")