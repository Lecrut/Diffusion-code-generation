from datetime import datetime

def get_day(date_str: str) -> str:
    if not isinstance(date_str, str):
        raise ValueError("Input must be a string")
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    sample_date = "2023-10-05"
    day_result = get_day(sample_date)
    print(day_result)