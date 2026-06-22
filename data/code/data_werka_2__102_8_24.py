from datetime import datetime, date

def is_weekday(date_string: str) -> bool:
    try:
        parsed = datetime.fromisoformat(date_string)
    except ValueError as e:
        raise ValueError(f'Invalid ISO format date string: {date_string}') from e
    weekday = parsed.weekday()
    return weekday < 5
if __name__ == '__main__':
    sample_dates = ['2023-10-07', '2023-10-08', '2023-10-09', '2023-10-10', '2023-10-11', '2023-10-12', '2023-10-13']
    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(result)