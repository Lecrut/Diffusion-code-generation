from datetime import date, datetime
from typing import Union
def calculate_days_delta(start: Union[str, datetime], end: Union[str, datetime]) -> int:
    def parse_date(d) -> date:
        if isinstance(d, str):
            return date.fromisoformat(d)
        elif isinstance(d, (datetime)):
            return d.date()
        else:
            raise TypeError("Input must be a string or datetime object")
    start_dt = parse_date(start)
    end_dt = parse_date(end)
    delta_days = int((end_dt - start_dt).days)
    return delta_days
if __name__ == '__main__':
    result1 = calculate_days_delta("2023-01-01", "2023-01-15")
    assert result1 == 14, f"Expected 14 days, got {result1}"
    dt_start = datetime(2023, 6, 1)
    dt_end = datetime(2023, 7, 5)
    result2 = calculate_days_delta(dt_start, dt_end)
    assert result2 == 34, f"Expected 34 days, got {result2}"
    print("All tests passed.")