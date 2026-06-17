import sys
from datetime import datetime
def process_date(date_input):
    try:
        date_obj = datetime.strptime(date_input, '%Y-%m-%d')
        if date_obj.time() == datetime.min.time():
            now = datetime.now()
            iso_date = f"{date_obj.strftime('%Y-%m-%d')}T{now.strftime('%H:%M:%S')}"
        else:
            iso_date = date_obj.isoformat()
        print(iso_date)
    except ValueError:
        print("Invalid date format provided.")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2024/01/15",
        "not-a-date"
    ]
    for date_str in sample_dates:
        process_date(date_str)