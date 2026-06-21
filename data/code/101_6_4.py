from dateutil.parser import parse

def get_weekday_name(date_string: str) -> str:
    if not date_string:
        raise ValueError("Input string cannot be empty")
    parsed_date = parse(date_string)
    return parsed_date.strftime('%A')

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    weekday = get_weekday_name(sample_date)
    print(weekday)