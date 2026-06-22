from dateutil.parser import parse
from datetime import datetime

def get_weekday_from_string(date_str: str) -> str:
    parsed_datetime: datetime = parse(date_str)
    day_index: int = parsed_datetime.weekday()
    days_of_week: list[str] = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    return days_of_week[day_index]

if __name__ == '__main__':
    input_date: str = 'January 15, 2023'
    computed_day: str = get_weekday_from_string(input_date)
    print(computed_day)