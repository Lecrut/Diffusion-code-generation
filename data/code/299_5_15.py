from datetime import date

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

if __name__ == '__main__':
    dates_to_check = [date(2023, 10, 9), date(2023, 10, 10), date(2023, 10, 11)]
    
    for dt in dates_to_check:
        if isinstance(dt, date):
            print(f"Is {dt} a weekend? {is_weekend(dt)}")
        else:
            print(f"{dt} is not a valid date.")