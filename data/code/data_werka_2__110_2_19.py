import datetime
import time

def sort_iso8601_dates(date_strings):
    if not date_strings:
        return []
    def to_timestamp(d_str):
        dt = datetime.datetime.fromisoformat(d_str)
        return dt.timestamp()
    return sorted(date_strings, key=to_timestamp)

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2021-05-15T08:30:00",
        "2023-01-20T18:45:00",
        "2022-12-31T23:59:59",
        "2020-02-29T00:00:00"
    ]
    sorted_dates = sort_iso8601_dates(dates)
    print(sorted_dates)