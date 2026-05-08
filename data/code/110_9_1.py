import sys
from datetime import datetime
if __name__ == '__main__':
    input_data = [
        "2023-10-26",
        "2024-01-15",
        "2023-05-01",
        "2024-03-10"
    ]
    date_objects = []
    for date_str in input_data:
        try:
            date_objects.append(datetime.strptime(date_str, "%Y-%m-%d"))
        except ValueError:
            pass
    date_objects.sort()
    iso_dates = [date.isoformat() for date in date_objects]
    for iso_date in iso_dates:
        print(iso_date)