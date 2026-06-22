def is_weekend_with_holidays(date):
    weekends = ['Saturday', 'Sunday']
    holidays = ['2023-12-25', '2024-01-01']
    return date.strftime('%A') in weekends or date.strftime('%Y-%m-%d') in holidays
if __name__ == '__main__':
    from datetime import datetime
    sample_date = datetime(2023, 12, 25)
    print(is_weekend_with_holidays(sample_date))