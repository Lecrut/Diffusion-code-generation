from datetime import date

def is_weekend_or_holiday(date_str):
    holidays = {'2023-10-13', '2023-10-14', '2023-10-15'}
    return date.fromisoformat(date_str).weekday() >= 5 or date_str in holidays

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-13'))
    print(is_weekend_or_holiday('2023-10-14'))
    print(is_weekend_or_holiday('2023-10-15'))