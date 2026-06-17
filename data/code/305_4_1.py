import sys
from datetime import datetime
if __name__ == '__main__':
    input_dates = [
        "2023-10-26",
        "2023-10-25",
        "2023-10-27",
        "2023-10-24"
    ]
    date_objects = []
    for date_str in input_dates:
        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            date_objects.append(date_obj)
        except ValueError:
            pass
    date_objects.sort()
    for date_obj in date_objects:
        print(date_obj.isoformat())