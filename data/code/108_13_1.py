import sys
from datetime import datetime
def process_date(date_string):
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        print(date_obj.day)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    sample_date = "2023-10-27"
    process_date(sample_date)