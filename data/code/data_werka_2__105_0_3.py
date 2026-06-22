from datetime import datetime, timedelta

def get_next_monday(reference_date=None):
    days_map = {
        0: 1,
        1: 0,
        2: 6,
        3: 5,
        4: 4,
        5: 3,
        6: 2,
    }
    if reference_date is None:
        reference_date = datetime.today()
    target_weekday = 0
    current_weekday = reference_date.weekday()
    delta_days = days_map.get(current_weekday, 0)
    if current_weekday == target_weekday:
        delta_days = 7
    next_monday = reference_date + timedelta(days=delta_days)
    return next_monday

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 23)
    result_date = get_next_monday(sample_date)
    print(result_date.strftime('%Y-%m-%d'))