import calendar
import datetime

def get_day_of_week(date_string: str) -> int:
    year_part = int(date_string[0:4])
    month_part = int(date_string[5:7])
    day_part = int(date_string[8:10])
    date_instance = datetime.date(year_part, month_part, day_part)
    return date_instance.isoweekday() % 7

if __name__ == '__main__':
    sample_date = "2024-05-15"
    result = get_day_of_week(sample_date)
    print(result)
    
    sample_date_2 = "2000-02-29"
    result_2 = get_day_of_week(sample_date_2)
    print(result_2)
    
    sample_date_3 = "2025-12-25"
    result_3 = get_day_of_week(sample_date_3)
    print(result_3)