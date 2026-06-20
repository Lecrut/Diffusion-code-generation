import datetime

WEEKDAY_THURSDAY = 3
START_DATE = "2023-09-15"

def find_next_thursday(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    days_until_thursday = (WEEKDAY_THURSDAY - start_date.weekday()) % 7
    next_thursday = start_date + datetime.timedelta(days=days_until_thursday)
    return next_thursday.strftime("%Y-%m-%d")

if __name__ == '__main__':
    sample_date_str = START_DATE
    result_date = find_next_thursday(sample_date_str)
    print(result_date)