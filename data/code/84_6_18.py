import calendar

def get_day_number(year: int, month: int, day: int) -> int:
    return calendar.timegm((year, month, day, 0, 0, 0)) // (60 * 60 * 24)

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 5
    print(get_day_number(sample_year, sample_month, sample_day))