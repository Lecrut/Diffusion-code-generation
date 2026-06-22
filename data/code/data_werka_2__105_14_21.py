import datetime

WEEKDAY_MONDAY = 0
WEEKS_IN_ADVANCE = 1

def calculate_next_monday():
    current_date = datetime.date.today()
    days_until_monday = (WEEKDAY_MONDAY - current_date.weekday()) % 7
    if days_until_monday == 0:
        days_until_monday = 7
    next_monday = current_date + datetime.timedelta(days=days_until_monday)
    return next_monday

if __name__ == '__main__':
    sample_result = calculate_next_monday()
    print(sample_result)