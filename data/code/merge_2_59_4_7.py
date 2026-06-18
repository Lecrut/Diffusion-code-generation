import datetime
def get_day_of_week(year: int, month: int, day: int) -> str:
    try:
        dt = datetime.datetime(year=year, month=month, day=day)
        return dt.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date {year}-{month}-{day}: {e}")
if __name__ == '__main__':
    SAMPLE_DATE = (2023, 10, 5)
    year, month, day = SAMPLE_DATE
    result_day_name = get_day_of_week(year, month, day)
    print(f"Date: {year}-{month:02d}-{day}")
    print(f"Day of Week: {result_day_name}")