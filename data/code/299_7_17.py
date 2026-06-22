from datetime import date

def is_weekend_or_holiday(date_str):
    holiday = date(2023, 10, 12)
    return date.fromisoformat(date_str).weekday() >= 5 or date_str == holiday.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-12'))