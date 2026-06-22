import datetime

def convert_date_format(date_str: str) -> str:
    try:
        dt_object = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
        return dt_object.strftime('%d-%b-%Y %I:%M %p')
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}': {e}")

if __name__ == '__main__':
    date1 = "2023-10-27T14:30:45.678901+00:00"
    print(f"Original Date: {date1}")
    try:
        formatted_date_1 = convert_date_format(date1)
        print(f"Converted to DD-Mon-YYYY HH:MM AM/PM: {formatted_date_1}")
    except ValueError as e:
        print(f"Error processing date 1: {e}")