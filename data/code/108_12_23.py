from datetime import datetime
from typing import Union

def get_day_number(iso_string: str) -> int:
    parsed_date = datetime.fromisoformat(iso_string)
    return parsed_date.day

if __name__ == '__main__':
    sample_input = '2024-07-04T12:00:00'
    computed_day = get_day_number(sample_input)
    print(computed_day)