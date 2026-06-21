from datetime import datetime

def sort_iso_dates(date_strings):
    if not date_strings:
        return []
    return sorted(date_strings, key=lambda x: datetime.fromisoformat(x))

if __name__ == '__main__':
    dates = [
        "2024-05-10T15:30:00",
        "2023-01-01T00:00:00",
        "2025-12-25T10:00:00",
        "2022-07-04T12:00:00"
    ]
    print(sort_iso_dates(dates))