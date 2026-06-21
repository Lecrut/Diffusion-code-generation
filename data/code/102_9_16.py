import datetime
import calendar

WEEKDAY_THRESHOLD = 5

def verify_date_is_weekday(date_string):
    parsed = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    weekday_number = parsed.weekday()
    return weekday_number < WEEKDAY_THRESHOLD

if __name__ == '__main__':
    check_dates = [
        "2023-10-01",
        "2023-10-02",
        "2023-10-07",
        "2023-10-08"
    ]
    outcomes = [verify_date_is_weekday(d) for d in check_dates]
    print(outcomes)