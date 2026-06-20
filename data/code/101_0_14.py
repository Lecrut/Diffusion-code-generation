import datetime

def validate_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_day_of_week(date_string):
    if not validate_date(date_string):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date_obj.strftime('%A')
    return day_of_week

if __name__ == '__main__':
    sample_date = '2023-10-05'
    print(get_day_of_week(sample_date))