from datetime import date
def calculate_day_difference(start_date: str | date, end_date: str | date) -> int:
    try:
        start = (start_date if isinstance(start_date, date) else date.fromisoformat(start_date))
        end = (end_date if isinstance(end_date, date) else date.fromisoformat(end_date))
        return (end - start).days
    except ValueError as e:
        raise ValueError(f"Invalid date format or out of range. Error details: {e}")
if __name__ == '__main__':
    result = calculate_day_difference("2023-01-01", "2024-05-20")
    print(result)