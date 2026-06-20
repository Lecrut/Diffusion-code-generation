import datetime

def get_day_of_week(date_str):
    try:
        date_obj = datetime.date.fromisoformat(date_str)
        return date_obj.weekday()
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}") from e

if __name__ == '__main__':
    sample_date = '2024-07-04'
    try:
        day_of_week = get_day_of_week(sample_date)
        print(day_of_week)
    except ValueError as e:
        print(e)