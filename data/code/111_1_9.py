from datetime import date, timedelta

DAYS_OFFSET = 30
BASE_YEAR = 2024
BASE_MONTH = 7
BASE_DAY = 4

def calculate_future_date():
    reference_date = date(BASE_YEAR, BASE_MONTH, BASE_DAY)
    duration = timedelta(days=DAYS_OFFSET)
    calculated_date = reference_date + duration
    return calculated_date.isoformat()

if __name__ == '__main__':
    print(calculate_future_date())