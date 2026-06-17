from datetime import date, timedelta
from typing import Optional
def subtract_years(d: date, years: int) -> date:
    if not isinstance(years, int):
        raise ValueError("Years must be an integer.")
    new_year = d.year - years
    try:
        return date(new_year, d.month, d.day)
    except ValueError as e:
        if "day" not in str(e):
            raise
        target_day = None
        while True:
            try:
                new_date = date(new_year, d.month, d.day)
                return new_date
            except ValueError as e_inner:
                if "day" in str(e_inner):
                    raise ValueError(f"Cannot subtract {years} years from {d}: Invalid calendar day in resulting year.")
if __name__ == '__main__':
    input_date = date(2024, 6, 15)
    years_to_subtract = 3
    try:
        result = subtract_years(input_date, years_to_subtract)
        print(f"Original Date: {input_date}")
        print(f"Deducted Years: {years_to_subtract}")
        print(f"Resulting Date: {result}")
    except ValueError as ve:
        print(f"Error occurred: {ve}")