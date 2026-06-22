from datetime import date

def get_remaining_days_in_month():
    current_date = date(2024, 5, 10)
    year = current_date.year
    month = current_date.month
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)
    end_of_current_month = next_month - date(1, 1, 1)
    delta = end_of_current_month - current_date
    return delta.days

if __name__ == '__main__':
    print(get_remaining_days_in_month())