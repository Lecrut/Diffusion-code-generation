from datetime import date
WEEKENDS = {5, 6}
HOLIDAYS = {'2023-10-13', '2023-10-14', '2023-10-15'}

def is_weekend_or_holiday(date_str):
    date_obj = date.fromisoformat(date_str)
    return date_obj.weekday() in WEEKENDS or date_str in HOLIDAYS
if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)