from datetime import date, timedelta

DAY_INDEX_SATURDAY = 5

def get_next_saturday(reference_date):
    current_weekday = reference_date.weekday()
    days_until_saturday = DAY_INDEX_SATURDAY - current_weekday
    if days_until_saturday <= 0:
        days_until_saturday += 7
    target_date = reference_date + timedelta(days=days_until_saturday)
    return target_date

if __name__ == '__main__':
    fixed_date = date(2023, 11, 1)
    computed_saturday = get_next_saturday(fixed_date)
    print(computed_saturday)