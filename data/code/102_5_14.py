import datetime

def has_weekdays(date_strings):
    weekdays = [dt for dt in date_strings if datetime.datetime.strptime(dt, "%Y-%m-%d").weekday() < 5]
    return len(weekdays) > 0

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-03"]
    result = has_weekdays(sample_dates)
    print(result)