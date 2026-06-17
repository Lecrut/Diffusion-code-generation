from datetime import date, timedelta
def validate_and_calculate(year: int) -> date:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    try:
        current_date = date.today()
        input_year = year - 10
    except ValueError as e:
        raise RuntimeError(f"Invalid year calculation: {e}") from e
    return (current_date + timedelta(days=-365)).replace(year=input_year)
if __name__ == '__main__':
    result = validate_and_calculate(2024)
    print(result)