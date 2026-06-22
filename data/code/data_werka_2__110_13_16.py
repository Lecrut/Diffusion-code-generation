from datetime import datetime

def sort_iso_dates(date_strings):
    return sorted(date_strings, key=lambda d: datetime.fromisoformat(d))

if __name__ == '__main__':
    dates = [
        "2023-10-01T12:00:00",
        "2021-01-15T08:30:00",
        "2023-09-30T23:59:59",
        "2022-05-20T14:15:00"
    ]
    result = sort_iso_dates(dates)
    print(result)