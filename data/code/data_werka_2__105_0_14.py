from datetime import datetime, timedelta

def get_next_monday(reference_date=None):
    if reference_date is None:
        reference_date = datetime.today()
    current_weekday = reference_date.weekday()
    if current_weekday == 0:
        target_date = reference_date + timedelta(days=7)
    else:
        days_to_add = 7 - current_weekday
        target_date = reference_date + timedelta(days=days_to_add)
    return target_date

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 25)
    result = get_next_monday(sample_date)
    print(result.strftime('%Y-%m-%d'))