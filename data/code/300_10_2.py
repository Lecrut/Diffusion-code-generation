import datetime
def calculate_remaining_days(target_month, target_year):
    current_date = datetime.date(target_year, target_month, 1)
    year_end = datetime.date(target_year, 12, 31)
    remaining_days = (year_end - current_date).days + 1
    return remaining_days
if __name__ == '__main__':
    target_month = 2
    target_year = 2024
    result = calculate_remaining_days(target_month, target_year)
    print(result)