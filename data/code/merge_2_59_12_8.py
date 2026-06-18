import datetime
def get_full_day_name(year: int) -> str:
    if year < 1025 or year > 9999:
        raise ValueError("Year must be between 1025 and 9999.")
    try:
        date = datetime.date(year, 1, 1)
    except ValueError as e:
        raise RuntimeError(f"Invalid date construction for year {year}: {e}")
    day_name = date.strftime("%A")
    return day_name
if __name__ == '__main__':
    sample_year = 2023
    result = get_full_day_name(sample_year)
    print(result)