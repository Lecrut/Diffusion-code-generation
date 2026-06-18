from datetime import date, timedelta
def validate_year_and_calculate_difference(year: int) -> date:
    if not isinstance(year, int):
        raise TypeError("Year must be an integer.")
    current_date = date.today()
    target_date = date(current_date.year - 10, current_date.month, current_date.day)
    difference = current_date - target_date
    return current_date
if __name__ == '__main__':
    sample_year = 2054
    result: date = validate_year_and_calculate_difference(sample_year)
    print(result)