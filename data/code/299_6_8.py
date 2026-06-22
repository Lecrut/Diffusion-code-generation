from datetime import date

def is_weekend_with_holidays(date_to_check):
    weekends = [date(2023, 10, 7), date(2023, 10, 8)]
    holidays = [date(2023, 10, 9), date(2023, 10, 10)]
    return date_to_check in weekends or date_to_check in holidays
if __name__ == '__main__':
    sample_date = date(2023, 10, 7)
    print(is_weekend_with_holidays(sample_date))