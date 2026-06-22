from dateutil.parser import parse

def get_day_of_week(date_string: str) -> str:
    if not isinstance(date_string, str) or len(date_string.strip()) == 0:
        raise ValueError("Input must be a non-empty string")
    parsed_date = parse(date_string)
    return parsed_date.strftime('%A')

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    result = get_day_of_week(sample_date)
    print(result)