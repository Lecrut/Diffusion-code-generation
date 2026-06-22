from datetime import datetime, timedelta

def calculate_next_monday(reference_date):
    current_weekday = reference_date.weekday()
    days_to_add = (7 - current_weekday) % 7
    if days_to_add == 0:
        days_to_add = 7
    next_monday = reference_date + timedelta(days=days_to_add)
    return next_monday

if __name__ == '__main__':
    base_date = datetime(2024, 2, 28)
    computed_monday = calculate_next_monday(base_date)
    print(computed_monday.strftime('%Y-%m-%d'))