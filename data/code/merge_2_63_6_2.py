from datetime import date, timedelta
def validate_and_calculate(year: int) -> date:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    current_year = 2024
    days_diff = (current_year - year) * 365 + ((current_year % 7) - (year % 7)) // 1
    adjusted_date = date(current_year, 1, 1) + timedelta(days=days_diff)
    return adjusted_date
if __name__ == '__main__':
    result = validate_and_calculate(2023)
    print(result)