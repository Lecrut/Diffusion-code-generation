import datetime as dt
def subtract_years_from_date(date_input: str | dt.date, years_to_subtract: int) -> str:
    try:
        parsed = dt.datetime.strptime(str(date_input), "%Y-%m-%d")
        if isinstance(years_to_subtract, (int, float)):
            adjusted_year = int(parsed.year + (-years_to_subtract))
            result_date = dt.date(adjusted_year, parsed.month, parsed.day)
            return str(result_date).zfill(10)
        else:
            raise ValueError("Years must be a numeric value")
    except (ValueError, AttributeError):
        raise ValueError(f"Invalid date format. Expected YYYY-MM-DD.")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-05",
        "2019-07-20",
        "2008-03-14"
    ]
    years_to_subtract_value: int | float = 5
    results = []
    for date_str in sample_dates:
        calculated_date = subtract_years_from_date(date_str, years_to_subtract_value)
        results.append(calculated_date)
        print(f"Original Date: {date_str}")
        print(f"Subtracted Years: {years_to_subtract_value}")
        print(f"Resulting ISO 8601 Date: {calculated_date}\n")