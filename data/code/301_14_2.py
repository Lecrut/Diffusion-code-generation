import sys
from datetime import datetime
def convert_to_iso8601(date_string):
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        now = datetime.now()
        return date_obj.strftime('%Y-%m-%dT%H:%M:%S')
    except ValueError:
        return "Invalid date format provided"
if __name__ == '__main__':
    sample_date = "2023-10-27"
    iso_time = convert_to_iso8601(sample_date)
    print(iso_time)