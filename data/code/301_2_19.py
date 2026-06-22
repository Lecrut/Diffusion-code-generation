from datetime import datetime

ISO_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

def convert_to_iso(date_string):
    try:
        dt_object = datetime.strptime(date_string, "%Y-%m-%d")
        return dt_object.strftime(ISO_FORMAT)
    except ValueError:
        return "Error: Invalid input format. Expected YYYY-MM-DD."

if __name__ == '__main__':
    date1 = "2023-10-27"
    print(convert_to_iso(date1))