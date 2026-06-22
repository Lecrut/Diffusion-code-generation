from datetime import date, timedelta

def calculate_upcoming_saturday(reference_date):
    days_to_add = (5 - reference_date.weekday()) % 7
    if days_to_add == 0 and reference_date.weekday() == 5:
        return reference_date
    return reference_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    fixed_start = date(2023, 11, 1)
    computed_date = calculate_upcoming_saturday(fixed_start)
    print(computed_date)