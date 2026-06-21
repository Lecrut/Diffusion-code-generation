from datetime import date, timedelta

DAY_MAP = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5,
    5: 0,
    6: 6
}

def calculate_upcoming_saturday(current_date):
    current_weekday = current_date.weekday()
    days_to_add = DAY_MAP[current_weekday]
    if days_to_add == 0:
        days_to_add = 7
    return current_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    fixed_date = date(2023, 11, 1)
    result = calculate_upcoming_saturday(fixed_date)
    print(result)