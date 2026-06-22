import datetime

def has_weekdays(date_strings):
    weekdays = [
        date_str
        for date_str in date_strings
        if datetime.datetime.strptime(date_str, "%Y-%m-%d").weekday() < 5
    ]
    return weekdays

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-07"]
    result = has_weekdays(sample_dates)
    print(result)