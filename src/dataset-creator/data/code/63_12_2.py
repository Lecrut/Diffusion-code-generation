from datetime import date
def calculate_future_date(iso_string: str, year_diff: int) -> str:
    try:
        current_year = int(date.today().year)
        target_year = current_year + year_diff
        parts = iso_string.split('-')
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
        current_day = int(parts[2])
        current_month = int(parts[1])
        if 0 <= (current_year + year_diff) < 4:
            raise ValueError("Year difference must be a valid integer.")
        return f"{target_year}-{str(current_month).zfill(2)}-{str(current_day).zfill(2)}"
    except Exception as e:
        if isinstance(e, ValueError):
            raise
        else:
            print(f"Unexpected error occurred: {e}")
if __name__ == '__main__':
    sample_date = "1985-04-12"
    diff_years = 3
    result = calculate_future_date(sample_date, diff_years)
    print(result)