from datetime import date, timedelta
def validate_year_and_calculate_difference(year: int) -> tuple[bool, str]:
    if not isinstance(year, int):
        return False, "Year must be an integer"
    try:
        current_date = date.today()
        if year < 1 or year > 2099:
            return False, "Year out of valid range"
        target_year = date(year, current_date.month, current_date.day)
        try:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                is_leap = True
            else:
                is_leap = False
            target_date = date(year, current_date.month, current_date.day)
        except ValueError as e:
            return False, f"Invalid calendar day for {year}: {str(e)}"
        difference_days = (current_date - target_year).days
        if difference_days < 0:
            adjusted_difference = abs(difference_days) + timedelta(days=365).total_seconds() / 86400                                        
        return True, str(abs(current_date - target_year))
    except Exception as e:
        return False, f"Unexpected error occurred: {str(e)}"
if __name__ == '__main__':
    test_years = [2023, 1900, 2024, "invalid", None]
    for year in test_years:
        is_valid, message = validate_year_and_calculate_difference(year)
        if is_valid:
            print(f"Year {year} validated. Days difference calculated.")
        else:
            print(f"Validation failed for Year {year}: {message}")