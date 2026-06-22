import calendar

DAY_INDEX_OFFSET = 0
MAX_MONTHS = 12
MAX_DAYS = 31
MIN_YEAR = 1
MAX_YEAR = 9999

def get_weekday_name(date_tuple):
    year, month, day = date_tuple
    if not (MIN_YEAR <= year <= MAX_YEAR):
        raise ValueError(f"Year out of range: {year}")
    if not (1 <= month <= MAX_MONTHS):
        raise ValueError(f"Month out of range: {month}")
    if not (1 <= day <= MAX_DAYS):
        raise ValueError(f"Day out of range: {day}")
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

if __name__ == '__main__':
    sample_date = (2024, 5, 15)
    result = get_weekday_name(sample_date)
    print(result)