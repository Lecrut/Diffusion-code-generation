from datetime import datetime
from typing import Union

def is_weekday(date_string: str) -> bool:
    dt = datetime.fromisoformat(date_string)
    return dt.weekday() < 5

if __name__ == '__main__':
    sample_dates = ["2023-10-07", "2023-10-08", "2023-10-09"]
    for date_str in sample_dates:
        result = is_weekday(date_str)
        print(result)