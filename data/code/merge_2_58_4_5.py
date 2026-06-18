from datetime import date, datetime
from typing import Union
def calculate_days_delta(start: Union[date, str], end: Union[date, str]) -> int:
    def parse_date(d) -> date:
        if isinstance(d, date):
            return d
        try:
            parsed = datetime.strptime(str(d), "%Y-%m-%d").date()
            return parsed
        except ValueError:
            raise TypeError("Invalid date format. Expected YYYY-MM-DD string or date object.")
    start_date = parse_date(start)
    end_date = parse_date(end)
    delta_days = (end_date - start_date).days
    if delta_days < 0:
        return abs(delta_days)
    return int(delta_days)
if __name__ == '__main__':
    result_1 = calculate_days_delta(date(2023, 1, 1), date(2023, 1, 5))
    assert result_1 == 4
    result_2 = calculate_days_delta("2023-06-15", "2023-07-01")
    expected_2 = (date(2023, 7, 1) - date(2023, 6, 15)).days
    assert result_2 == expected_2
    result_3 = calculate_days_delta("2024-12-31", "2024-01-01")
    assert abs(result_3) == (date(2024, 12, 31) - date(2024, 1, 1)).days
    print("All tests passed.")