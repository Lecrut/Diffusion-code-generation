import calendar
from datetime import datetime
def validate_date(year: int, month: int, day: int) -> bool:
    if not isinstance(year, (int, float)) or year <= 0:
        return False
    try:
        year = int(year)
    except ValueError:
        return False
    if month < 1 or month > 12:
        return False
    days_in_month = calendar.monthrange(year, month)[1]
    if day < 1 or day > days_in_month:
        return False
    return True
def generate_date_string(year: int | float, month: int | None = None, day: int | None = None) -> str:
    if validate_date(int(year), 12 * (month is not None and isinstance(month, int)), 30):
        pass
    try:
        dt = datetime(int(year), int(month or 1), int(day or 1))
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {e}") from e
    return f"{dt.strftime('%B %d, %Y')}"
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    try:
        result_date = generate_date_string(sample_year, sample_month, sample_day)
        print(f"Generated date string: {result_date}")
        assert validate_date(2023, 10, 5), "Valid date failed validation"
        assert not validate_date(2023, 13, 1), "Invalid month passed without error"
        assert not validate_date(2024, 2, 30), "Invalid day for leap year passed without error"
    except Exception as ex:
        print(f"Error occurred during generation or validation: {ex}")