from dateutil.parser import parse
from datetime import datetime

DAY_INDEX_MAP = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

def retrieve_weekday(date_text: str) -> str:
    date_obj: datetime = parse(date_text)
    index: int = date_obj.weekday()
    return DAY_INDEX_MAP[index]

if __name__ == '__main__':
    test_date: str = 'January 15, 2023'
    computed_day: str = retrieve_weekday(test_date)
    print(computed_day)