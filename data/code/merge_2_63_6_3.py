from datetime import date, timedelta
def validate_year_and_calculate_difference(year: int) -> tuple[date, str]:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    current_date = date.today()
    target_date = date(current_date.year - year + 1900, current_date.month, current_date.day)
    difference_days = (current_date - target_date).days
    return current_date, f"Days before adjusted datetime: {difference_days}"
if __name__ == '__main__':
    sample_year = 50
    final_result = validate_year_and_calculate_difference(sample_year)
    print(final_result[0])
    print(final_result[1])