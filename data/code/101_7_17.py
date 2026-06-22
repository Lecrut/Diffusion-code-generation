import datetime

REFERENCE_DATE = datetime.date(2024, 7, 4)
DAY_OFFSET = 0

def calculate_weekday_index(reference_date: datetime.date, offset: int = 0) -> int:
    target_date = reference_date + datetime.timedelta(days=offset)
    return target_date.weekday()

if __name__ == '__main__':
    weekday_index = calculate_weekday_index(REFERENCE_DATE, DAY_OFFSET)
    print(weekday_index)