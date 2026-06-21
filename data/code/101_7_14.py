import datetime
import calendar

def compute_weekday_index(date_str):
    if not isinstance(date_str, str):
        raise ValueError("date_str must be a string")
    try:
        parsed_date = datetime.date.fromisoformat(date_str)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")
    return parsed_date.weekday()

if __name__ == '__main__':
    sample_date = '2024-07-04'
    weekday_index = compute_weekday_index(sample_date)
    print(weekday_index)