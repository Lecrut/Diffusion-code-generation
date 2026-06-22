from datetime import date, timedelta
from typing import Union

def is_monday_through_friday(target_date: Union[date, str]) -> bool:
    if isinstance(target_date, str):
        try:
            year, month, day = map(int, target_date.split('-'))
            parsed_date = date(year, month, day)
        except (ValueError, AttributeError) as e:
            raise ValueError(f"Invalid date string format: {target_date}") from e
    elif isinstance(target_date, date):
        parsed_date = target_date
    else:
        raise TypeError(f"Expected date or string, got {type(target_date)}")
    
    start_of_week = parsed_date - timedelta(days=parsed_date.weekday())
    end_of_week = start_of_week + timedelta(days=4)
    
    return start_of_week <= parsed_date <= end_of_week

if __name__ == '__main__':
    test_cases = [
        date(2023, 10, 23),
        date(2023, 10, 28),
        "2023-10-29",
        date(2023, 10, 30),
        date(2023, 10, 31),
    ]
    for tc in test_cases:
        print(is_monday_through_friday(tc))