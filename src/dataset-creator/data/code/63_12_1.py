from datetime import date
def calculate_future_date(iso_string: str, year_diff: int) -> str:
    try:
        current_year = int(date.fromisoformat(iso_string).year) + year_diff
        return f"{current_year}-01-01"
    except ValueError as e:
        raise TypeError(f"Invalid input. Expected valid ISO date and integer.") from e
if __name__ == '__main__':
    result = calculate_future_date("2023-06-15", 5)
    print(result)