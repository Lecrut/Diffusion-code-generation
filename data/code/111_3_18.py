from datetime import date

def subtract_three_months(input_date):
    target_month = input_date.month - 3
    target_year = input_date.year
    if target_month <= 0:
        target_year -= 1
        target_month += 12
    max_days = [31, 29 if (target_year % 4 == 0 and target_year % 100 != 0) or (target_year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][target_month - 1]
    target_day = min(input_date.day, max_days)
    return date(target_year, target_month, target_day)

if __name__ == '__main__':
    sample_date = date(2023, 10, 15)
    computed_date = subtract_three_months(sample_date)
    print(computed_date)