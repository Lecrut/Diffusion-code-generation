from datetime import date
def subtract_years(input_date: date, years_to_subtract: int) -> date:
    if not isinstance(input_date, date):
        raise TypeError(f"Expected 'date' object, got {type(input_date).__name__}")
    if not isinstance(years_to_subtract, int) or isinstance(years_to_subtract, bool):
        raise TypeError("years_to_subtract must be an integer")
    if years_to_subtract < 0:
        raise ValueError("years_to_subtract cannot be negative")
    return input_date.replace(year=input_date.year - years_to_subtract)
if __name__ == '__main__':
    sample_input = date(2023, 12, 31)
    result = subtract_years(sample_input, 5)
    print(result)