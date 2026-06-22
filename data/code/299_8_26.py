from datetime import date

def is_weekend_or_holiday(date_str):
    holiday_dates = {'2023-10-13', '2023-10-14', '2023-10-15'}
    dt = date.fromisoformat(date_str)
    return dt.weekday() >= 5 or date_str in holiday_dates

if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)