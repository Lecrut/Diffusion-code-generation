from datetime import datetime
from typing import Union

DAY_LOOKUP = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 6,
    6: 7,
    7: 8,
    8: 9,
    9: 10,
    10: 11,
    11: 12,
    12: 13,
    13: 14,
    14: 15,
    15: 16,
    16: 17,
    17: 18,
    18: 19,
    19: 20,
    20: 21,
    21: 22,
    22: 23,
    23: 24,
    24: 25,
    25: 26,
    26: 27,
    27: 28,
    28: 29,
    29: 30,
    30: 31,
    31: 31,
}

def get_day_of_month(dt: Union[datetime, str]) -> int:
    parsed_dt = None
    if isinstance(dt, datetime):
        parsed_dt = dt
    elif isinstance(dt, str):
        try:
            parsed_dt = datetime.strptime(dt, "%Y-%m-%d")
        except ValueError as ve:
            raise ValueError(f"Invalid date string format: {dt}") from ve
    else:
        raise ValueError(f"Unsupported input type: {type(dt)}")
    
    day_num = parsed_dt.day
    return DAY_LOOKUP.get(day_num, day_num)

if __name__ == '__main__':
    sample_input = "2024-02-29"
    computed_day = get_day_of_month(sample_input)
    print(computed_day)