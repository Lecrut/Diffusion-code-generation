import datetime
import time

def sort_iso8601_dates(date_strings):
    parsed_dates = []
    for date_str in date_strings:
        dt = datetime.datetime.fromisoformat(date_str)
        timestamp = dt.timestamp()
        parsed_dates.append((timestamp, date_str))
    
    parsed_dates.sort(key=lambda x: x[0])
    
    sorted_dates = [item[1] for item in parsed_dates]
    return sorted_dates

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2022-01-15T08:30:00",
        "2024-05-20T18:45:00",
        "2023-01-01T00:00:00",
        "2023-10-01T12:00:00"
    ]
    result = sort_iso8601_dates(dates)
    print(result)