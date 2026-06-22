import datetime
import time

def sort_iso8601_dates(date_strings):
    def parse_to_timestamp(date_str):
        dt = datetime.datetime.fromisoformat(date_str)
        return dt.timestamp()

    sorted_dates = sorted(date_strings, key=parse_to_timestamp)
    return sorted_dates

if __name__ == '__main__':
    sample_dates = [
        "2023-10-01T12:00:00",
        "2021-05-15T08:30:00",
        "2023-01-20T18:45:00",
        "2022-12-31T23:59:59",
        "2020-02-29T00:00:00"
    ]

    result = sort_iso8601_dates(sample_dates)
    print(result)