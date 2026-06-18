from datetime import date
def get_day_of_week(year: int, month: int, day: int) -> str:
    try:
        d = date(year, month, day)
        return d.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date {year}-{month}-{day}: {e}")
if __name__ == '__main__':
    year_sample = 2023
    month_sample = 10
    day_sample = 5
    result_day_of_week = get_day_of_week(year_sample, month_sample, day_sample)
    print(f"Date: {year_sample}-{month_sample:02d}-{day_sample}")
    print(f"Day of Week: {result_day_of_week}")