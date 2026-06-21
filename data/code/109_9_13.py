from datetime import date

MONTH_DAYS = 31
START_DAY = 1
REFERENCE_YEAR = 2024
REFERENCE_MONTH = 7
REFERENCE_DAY = 10

def get_remaining_days_in_month(reference_date, month_length):
    days_elapsed = reference_date.day - START_DAY
    remaining = month_length - days_elapsed
    return remaining

if __name__ == '__main__':
    current_date = date(REFERENCE_YEAR, REFERENCE_MONTH, REFERENCE_DAY)
    result = get_remaining_days_in_month(current_date, MONTH_DAYS)
    print(result)