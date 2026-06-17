import calendar
def get_day_of_month(year, month):
    try:
        if not isinstance(year, int) or not isinstance(month, int):
            raise ValueError("Year and month must be integers.")
        if not (1 <= month <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1900 <= year <= 2100):
            raise ValueError("Year must be within a reasonable range (1900-2100).")
        day = calendar.day(year, month)
        return day
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    result = get_day_of_month(sample_year, sample_month)
    print(result)