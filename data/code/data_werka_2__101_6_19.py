from dateutil.parser import parse

WEEKDAY_FORMAT_CODE = "%A"

def get_day_of_week(date_string: str) -> str:
    parsed_date = parse(date_string)
    return parsed_date.strftime(WEEKDAY_FORMAT_CODE)

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    result = get_day_of_week(sample_date)
    print(result)