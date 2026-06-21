from datetime import date

DAYS_IN_WEEK = 7
MONTHS_IN_YEAR = 12

def calculate_remaining_days():
    current_date = date(2024, 5, 10)
    last_day_of_month = date(2024, 5, 31)
    remaining = last_day_of_month - current_date
    return remaining.days

if __name__ == '__main__':
    result = calculate_remaining_days()
    print(result)