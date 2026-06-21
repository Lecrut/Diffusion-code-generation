from datetime import date

def get_remaining_days_in_current_month():
    current_date = date(2024, 5, 20)
    if current_date.month == 12:
        last_day_of_month = date(current_date.year + 1, 1, 1)
    else:
        last_day_of_month = date(current_date.year, current_date.month + 1, 1)
    days_remaining = (last_day_of_month - current_date).days
    if days_remaining < 0:
        raise ValueError("Invalid date progression")
    return days_remaining

if __name__ == '__main__':
    print(get_remaining_days_in_current_month())