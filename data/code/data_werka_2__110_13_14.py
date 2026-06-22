from datetime import datetime

def sort_iso_dates(date_strings):
    return sorted(date_strings, key=lambda d: datetime.fromisoformat(d))

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2021-05-15T08:30:00",
        "2023-01-20T15:45:00",
        "2022-12-31T23:59:59"
    ]
    sorted_dates = sort_iso_dates(dates)
    print(sorted_dates)