from datetime import datetime

def get_day_of_month(date_string: str) -> int:
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        return date_object.day
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

if __name__ == '__main__':
    date_str = "2024-07-04"
    print(f"Day of the month for {date_str}: {get_day_of_month(date_str)}")