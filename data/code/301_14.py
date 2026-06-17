import sys
from datetime import datetime
def process_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        if date_obj.time() == datetime.min.time():
            now = datetime.now()
            iso_date = f"{date_obj.strftime('%Y-%m-%d')}T{now.strftime('%H:%M:%S')}"
        else:
            iso_date = date_obj.isoformat()
        print(iso_date)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    sample_date_input = "2023-10-27"
    process_date(sample_date_input)