from calendar import isleap
from datetime import date

def get_day_of_week(date_string: str) -> int:
    year_part = int(date_string[:4])
    month_part = int(date_string[5:7])
    day_part = int(date_string[8:10])
    target_date = date(year_part, month_part, day_part)
    return target_date.weekday()

if __name__ == '__main__':
    sample_date_1 = "2025-05-01"
    sample_date_2 = "2020-02-29"
    sample_date_3 = "1900-01-01"
    print(get_day_of_week(sample_date_1))
    print(get_day_of_week(sample_date_2))
    print(get_day_of_week(sample_date_3))