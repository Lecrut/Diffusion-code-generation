from datetime import datetime

def get_day_of_month(date_string: str) -> int:
    try:
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        return date_object.day
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date_str = "2024-07-04"
    try:
        day_of_month = get_day_of_month(date_str)
        print(f"The day of the month for {date_str} is: {day_of_month}")
    except ValueError as e:
        print(e)