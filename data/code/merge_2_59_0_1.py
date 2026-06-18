import datetime
def get_day_of_week(date_string: str) -> int:
    try:
        date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.weekday()
    except ValueError as e:
        raise ValueError(f"Invalid date format or year/month/day combination. Error: {e}")
if __name__ == '__main__':
    sample_dates = ['2023-10-05', '2024-07-20', '1998-06-15']
    for date_str in sample_dates:
        day_num = get_day_of_week(date_str)
        days_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
        print(f"Date: {date_str} -> Day of Week ({days_map[day_num]})")