import datetime

def get_day_of_week(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%A')
    except ValueError:
        raise ValueError(f"Invalid date format: {date_string}. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    sample_date = '2023-12-25'
    try:
        day_name = get_day_of_week(sample_date)
        print(day_name)
    except ValueError as e:
        print(f"Error: {e}")