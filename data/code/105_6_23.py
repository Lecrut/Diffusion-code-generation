from datetime import date, timedelta
import calendar

MULTIPLIER = 7
START_YEAR = 2024
START_MONTH = 1
START_DAY = 1

def calculate_next_multiple_date(start: date) -> date:
    days_in_month = calendar.monthrange(start.year, start.month)[1]
    current_day = START_DAY
    current_month = START_MONTH
    current_year = START_YEAR
    total_days_elapsed = 0
    while True:
        if total_days_elapsed > 0 and total_days_elapsed % MULTIPLIER == 0:
            return date(current_year, current_month, current_day)
        current_day += 1
        total_days_elapsed += 1
        if current_day > days_in_month:
            current_month += 1
            if current_month > 12:
                current_month = 1
                current_year += 1
            current_day = 1
            days_in_month = calendar.monthrange(current_year, current_month)[1]
if __name__ == '__main__':
    start_date = date(START_YEAR, START_MONTH, START_DAY)
    result = calculate_next_multiple_date(start_date)
    print(result)