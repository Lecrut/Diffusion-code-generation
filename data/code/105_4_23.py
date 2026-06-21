from datetime import date, timedelta

def find_nearest_saturday(reference_date):
    days_ahead = 5 - reference_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    next_saturday = reference_date + timedelta(days=days_ahead)
    return next_saturday

if __name__ == '__main__':
    start_date = date(2023, 11, 1)
    result = find_nearest_saturday(start_date)
    print(result)