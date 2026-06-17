from datetime import date
def map_date_to_day(year, month, day):
    try:
        d = date(year, month, day)
        return f"{d.strftime('%A')} ({d.strftime('%a')})"
    except ValueError as e:
        raise ValueError(f"Invalid date {year}-{month}-{day}: {e}")
if __name__ == '__main__':
    SAMPLE_DATE = (2023, 10, 5)
    result = map_date_to_day(*SAMPLE_DATE)
    print(f"Date: {'-'.join(map(str, SAMPLE_DATE))}")
    print(f"Day of Week: {result}")