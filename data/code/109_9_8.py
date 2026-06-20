import datetime

def calculate_remaining_days(current_date):
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                     7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if (current_date.year % 4 == 0 and current_date.year % 100 != 0) or (current_date.year % 400 == 0):
        days_in_month[2] = 29
    remaining_days = days_in_month[current_date.month] - current_date.day
    if current_date.month < 12:
        return remaining_days
    else:
        return 365 if (current_date.year % 4 == 0 and current_date.year % 100 != 0) or (current_date.year % 400 == 0) else 364

if __name__ == '__main__':
    current_date = datetime.date(2024, 6, 1)
    days_remaining = calculate_remaining_days(current_date)
    print(days_remaining)