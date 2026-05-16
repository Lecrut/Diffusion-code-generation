import sys
from datetime import datetime
if __name__ == '__main__':
    input_data = [
        "2023-10-26",
        "2023-10-25",
        "2023-10-27",
        "2023-10-24"
    ]
    date_objects = []
    for date_str in input_data:
        try:
            date_objects.append(datetime.strptime(date_str, "%Y-%m-%d"))
        except ValueError:
            pass
    date_objects.sort()
    for dt in date_objects:
        print(dt.isoformat())