from dateutil import parser

def validate_date_format(date_str):
    try:
        parser.parse(date_str)
        return True
    except ValueError:
        return False

def get_day_of_week(date_str):
    if not validate_date_format(date_str):
        raise ValueError("Invalid date format")
    
    date_obj = parser.parse(date_str)
    day_of_week = date_obj.strftime('%A')
    return day_of_week

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    print(get_day_of_week(sample_date))