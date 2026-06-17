import datetime
def get_full_day_name(year: int, month: int, day: int) -> str:
    try:
        if year < 1 or year > 9999:
            raise ValueError("Year must be between 1 and 9999.")
        date_obj = datetime.date(year, month, day)
        return date_obj.strftime("%A")
    except (ValueError, TypeError):
        raise ValueError(f"Invalid calendar input for {year}-{month}-{day}. Please check the format.")
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 12
    sample_day = 25
    try:
        day_name = get_full_day_name(sample_year, sample_month, sample_day)
        print(day_name)
    except ValueError as e:
        print(f"Error: {e}")