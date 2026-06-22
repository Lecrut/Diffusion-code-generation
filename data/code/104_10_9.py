from datetime import date
from typing import Union

RELATIONSHIP_MAP: dict[int, int] = {
    1: 1,
    0: 0,
    -1: -1,
}

def compare_dates(first: date, second: date) -> int:
    if not isinstance(first, date) or not isinstance(second, date):
        raise ValueError("Inputs must be datetime.date objects")
    
    diff: int = (first - second).days
    result: int = 1 if diff > 0 else (-1 if diff < 0 else 0)
    
    return RELATIONSHIP_MAP[result]

if __name__ == '__main__':
    start_date: date = date(2024, 5, 15)
    end_date: date = date(2024, 5, 10)
    
    outcome: int = compare_dates(start_date, end_date)
    print(outcome)
    
    same_date: date = date(2024, 5, 15)
    equality: int = compare_dates(start_date, same_date)
    print(equality)