import datetime

DATE_FORMAT_INPUT = "%Y-%m-%dT%H:%M:%S.%f%z"
DATE_FORMAT_OUTPUT = "%d-%b-%Y %I:%M %p"

def convert_date_format(date_str: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(date_str, DATE_FORMAT_INPUT)
        return dt_object.strftime(DATE_FORMAT_OUTPUT)
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}' with format '{DATE_FORMAT_INPUT}': {e}")

if __name__ == '__main__':
    date1 = "2023-10-27T14:30:00.123456+08:00"
    print(f"Original Date: {date1}")
    try:
        formatted_date_1 = convert_date_format(date1)
        print(f"Converted to DD-Mon-YYYY HH:MM AM/PM: {formatted_date_1}")
    except ValueError as e:
        print(f"Error processing date 1: {e}")

    date2 = "2023-11-05T09:45:00.678901-05:00"
    print(f"\nOriginal Date: {date2}")
    try:
        formatted_date_2 = convert_date_format(date2)
        print(f"Converted to DD-Mon-YYYY HH:MM AM/PM: {formatted_date_2}")
    except ValueError as e:
        print(f"Error processing date 2: {e}")