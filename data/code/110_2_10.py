import datetime
import time

def sort_iso8601_dates(date_strings):
    def parse_to_timestamp(date_str):
        dt = datetime.datetime.fromisoformat(date_str)
        return dt.timestamp()

    sorted_dates = sorted(date_strings, key=parse_to_timestamp)
    return sorted_dates

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2021-01-15T08:30:00",
        "2023-10-01T12:00:00",
        "2022-05-20T18:45:00",
        "2020-12-31T23:59:59"
    ]
    result = sort_iso8601_dates(dates)
    print(result)