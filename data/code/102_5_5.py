import datetime

def contains_weekdays(date_strings):
    weekdays = [
        datetime.datetime.strptime(d, "%Y-%m-%d").weekday() < 5
        for d in date_strings
    ]
    return any(weekdays)

if __name__ == '__main__':
    dates = ["2023-10-01", "2023-10-02", "2023-10-07"]
    result = contains_weekdays(dates)
    print(result)