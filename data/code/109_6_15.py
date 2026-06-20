import datetime

def calculate_remaining_fraction(current_date, target_month):
    current_year = current_date.year
    current_month = current_date.month
    if target_month > current_month:
        target_year = current_year
        target_month_num = target_month
    else:
        target_year = current_year - 1
        target_month_num = target_month + 12

    target_date = datetime.date(target_year, target_month_num, 1)
    days_in_current_month = (datetime.date(current_year, current_month, 1) +
                             datetime.timedelta(days=31)).replace(day=1) - datetime.date(current_year, current_month, 1)
    days_in_target_month = (target_date + datetime.timedelta(days=31)).replace(day=1) - target_date
    return days_in_current_month / days_in_target_month if days_in_target_month != 0 else None

if __name__ == '__main__':
    sample_date = datetime.date(2023, 4, 15)
    sample_target_month = 6
    print(calculate_remaining_fraction(sample_date, sample_target_month))