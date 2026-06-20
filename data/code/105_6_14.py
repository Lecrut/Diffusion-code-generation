import datetime

WEEK_DAYS = 7
START_DATE = datetime.date(2024, 1, 1)

def next_multiple_of_weeks(date):
    days_since_start = (date - START_DATE).days
    remainder = days_since_start % WEEK_DAYS
    if remainder == 0:
        return date
    return date + datetime.timedelta(days=WEEK_DAYS - remainder)

if __name__ == '__main__':
    sample_date = START_DATE + datetime.timedelta(days=15)
    next_week_day = next_multiple_of_weeks(sample_date)
    print(next_week_day)