from datetime import date

def is_weekend_or_holiday(date_str):
    try:
        parsed_date = date.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    
    holidays = {'2023-10-13', '2023-10-14', '2023-10-15'}
    day_of_week = parsed_date.weekday()
    return day_of_week >= 5 or date_str in holidays

if __name__ == '__main__':
    dates_to_check = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = {date: is_weekend_or_holiday(date) for date in dates_to_check}
    print(results)