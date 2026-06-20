from datetime import datetime

def sort_iso8601_dates(date_strings):
    return sorted(date_strings, key=lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%S"))

if __name__ == '__main__':
    dates = ["2023-04-01T12:00:00", "2023-03-31T23:59:59", "2023-04-02T00:00:00"]
    sorted_dates = sort_iso8601_dates(dates)
    print(sorted_dates)