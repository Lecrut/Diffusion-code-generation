from datetime import datetime

def sort_iso_dates(date_strings):
    return sorted(date_strings, key=lambda x: datetime.fromisoformat(x))

if __name__ == '__main__':
    dates = ["2023-04-15T12:30:00", "2023-04-10T09:00:00", "2023-04-20T18:45:00"]
    sorted_dates = sort_iso_dates(dates)
    print(sorted_dates)