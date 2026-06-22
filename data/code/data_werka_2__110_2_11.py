import datetime
import time

def sort_iso_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        dt = datetime.datetime.fromisoformat(date_str)
        ts = dt.timestamp()
        parsed_dates.append((ts, date_str))
    parsed_dates.sort(key=lambda x: x[0])
    return [item[1] for item in parsed_dates]

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2021-01-15T08:30:00",
        "2023-10-01T12:00:00",
        "2022-05-20T18:45:00"
    ]
    sorted_dates = sort_iso_dates(dates)
    print(sorted_dates)