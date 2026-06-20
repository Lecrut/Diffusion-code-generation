import datetime

def validate_datetime(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def calculate_duration(date1_str, date2_str):
    date1 = validate_datetime(date1_str)
    date2 = validate_datetime(date2_str)
    time_difference = abs(date2 - date1)
    return time_difference

if __name__ == '__main__':
    result = calculate_duration('2023-10-01', '2023-09-30')
    print(result.days)