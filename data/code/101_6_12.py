import calendar
from dateutil.parser import parse

def get_day_of_week(date_string: str) -> str:
    if not isinstance(date_string, str) or not date_string.strip():
        raise ValueError("Input must be a non-empty string")
    
    parsed_date = parse(date_string)
    day_index = parsed_date.weekday()
    
    return calendar.day_name[day_index]

if __name__ == '__main__':
    sample_input = 'January 15, 2023'
    output = get_day_of_week(sample_input)
    print(output)