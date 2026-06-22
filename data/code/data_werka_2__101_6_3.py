from datetime import date
from dateutil.parser import parse

def extract_weekday(date_input: str) -> str:
    parsed_obj = parse(date_input)
    weekday_number = parsed_obj.weekday()
    weekday_names = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    return weekday_names[weekday_number]

if __name__ == '__main__':
    target_date = 'January 15, 2023'
    day_name = extract_weekday(target_date)
    print(day_name)