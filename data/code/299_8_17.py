from datetime import date

HOLIDAYS = {'2023-10-13', '2023-10-14', '2023-10-15'}

def is_weekend_or_holiday(date_str):
    day_of_week = date.fromisoformat(date_str).weekday()
    return day_of_week >= 5 or date_str in HOLIDAYS

if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = [is_weekend_or_holiday(date) for date in dates_to_check]
    print(results)