import datetime
import calendar

WEEKDAY_MAP = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

def get_day_of_week_for_specific_date(year: int, month: int, day: int) -> str:
    try:
        date_instance = datetime.date(year, month, day)
        weekday_index = date_instance.weekday()
        return WEEKDAY_MAP[weekday_index]
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {e}") from e

if __name__ == '__main__':
    year_val = 2025
    month_val = 3
    day_val = 15
    computed_day = get_day_of_week_for_specific_date(year_val, month_val, day_val)
    print(computed_day)