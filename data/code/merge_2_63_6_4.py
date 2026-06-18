from datetime import date, timedelta
def validate_year_and_calculate_difference(year: int) -> tuple[date, str]:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    try:
        current_date = date.today()
        target_year_end = current_date.replace(year=year, month=12, day=31)
        delta_days = (target_year_end - current_date).days
        return date.today(), f"Days until end of {year}: {delta_days}"
    except ValueError:
        raise
if __name__ == '__main__':
    sample_year = 2025
    final_date, message = validate_year_and_calculate_difference(sample_year)
    print(f"Final Date: {final_date}")
    print(message)