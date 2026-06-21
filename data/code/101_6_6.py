from dateutil.parser import parse

DAY_INDEX_MAP = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def get_day_of_week(date_string: str) -> str:
    parsed_date = parse(date_string)
    index = parsed_date.weekday()
    return DAY_INDEX_MAP[index]

if __name__ == '__main__':
    sample_date = 'January 15, 2023'
    result = get_day_of_week(sample_date)
    print(result)