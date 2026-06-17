from datetime import date
def calculate_days_difference(start: str | date, end: str | date) -> int:
    try:
        start_date = parse_date(start)
        end_date = parse_date(end)
        return (end_date - start_date).days
    except ValueError as e:
        raise ValueError(f"Invalid date format or values: {e}")
def parse_date(date_input: str | date) -> date:
    if isinstance(date_input, date):
        return date_input
    try:
        return date.fromisoformat(date_input)
    except ValueError:
        parts = date_input.split('-')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return date(year, month, day)
if __name__ == '__main__':
    start_str = "2023-05-01"
    end_str = "2024-06-15"
    result = calculate_days_difference(start_str, end_str)
    print(result)