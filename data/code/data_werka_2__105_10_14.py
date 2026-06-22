from datetime import datetime, timedelta
from calendar import monthrange

DAY_DELTA = 1
INPUT_FORMAT = '%Y-%m-%d'

def get_next_day(date_str: str) -> datetime:
    parsed_date = datetime.strptime(date_str, INPUT_FORMAT)
    return parsed_date + timedelta(days=DAY_DELTA)

if __name__ == '__main__':
    sample_date = '2023-10-31'
    result = get_next_day(sample_date)
    print(result)