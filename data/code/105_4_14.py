import datetime

WEEKDAY_SATURDAY = 5

def nearest_upcoming_saturday(start_date):
    days_until_next_saturday = (WEEKDAY_SATURDAY - start_date.weekday()) % 7
    if days_until_next_saturday == 0:
        days_until_next_saturday += 7
    return start_date + datetime.timedelta(days=days_until_next_saturday)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 11, 1)
    next_saturday = nearest_upcoming_saturday(sample_date)
    print(f"Nearest upcoming Saturday after {sample_date}: {next_saturday}")