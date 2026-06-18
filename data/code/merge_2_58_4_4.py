from datetime import date, datetime
from typing import Union
def calculate_delta_days(start: Union[date, str], end: Union[date, str]) -> int:
    def parse_date(d: Union[date, str]) -> date:
        if isinstance(d, date):
            return d
        try:
            dt = datetime.strptime(d, "%Y-%m-%d")
            return dt.date()
        except ValueError as e:
            raise TypeError(f"Invalid date format. Expected 'YYYY-MM-DD' or a date object.") from e
    start_date = parse_date(start)
    end_date = parse_date(end)
    delta_days = (end_date - start_date).days
    return int(delta_days)
if __name__ == '__main__':
    result_1 = calculate_delta_days("2023-01-01", "2023-01-15")
    d_start = date(2024, 6, 1)
    d_end = date(2024, 6, 10)
    result_2 = calculate_delta_days(d_start, d_end)
    print(f"Test Case 1 (Strings): {result_1} days")
    print(f"Test Case 2 (Date Objects): {result_2} days")