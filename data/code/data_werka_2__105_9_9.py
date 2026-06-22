from datetime import datetime, timedelta

def compute_next_monday(input_date):
    current_weekday = input_date.weekday()
    days_to_add = 7 - current_weekday
    if current_weekday == 0:
        days_to_add = 7
    target_date = input_date + timedelta(days=days_to_add)
    return target_date

if __name__ == '__main__':
    base_date = datetime(2024, 2, 28)
    calculated_monday = compute_next_monday(base_date)
    print(calculated_monday.strftime('%Y-%m-%d'))