import calendar

def get_day_of_month(year, month, day):
    try:
        if not (1 <= year <= 9999) or not (1 <= month <= 12) or not (1 <= day <= 31):
            raise ValueError("Invalid date values")
        _, last_day = calendar.monthrange(year, month)
        if not (1 <= day <= last_day):
            raise ValueError("Day out of range for the given month and year")
        return day
    except ValueError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 15
    result = get_day_of_month(sample_year, sample_month, sample_day)
    if result is not None:
        print(f"Day {result} of Month {sample_month} in the year {sample_year}")