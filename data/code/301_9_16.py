import datetime

def convert_date_format(date_str: str) -> str:
    from_format = '%Y-%m-%dT%H:%M:%S.%f%z'
    to_format = '%d-%b-%Y %I:%M %p'
    try:
        dt_object = datetime.datetime.strptime(date_str, from_format)
        return dt_object.strftime(to_format)
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}' with format '{from_format}': {e}")

if __name__ == '__main__':
    sample_date = "2023-10-27T14:30:45.678901+08:00"
    print(f"Original Date: {sample_date}")
    try:
        formatted_date = convert_date_format(sample_date)
        print(f"Converted to DD-Mon-YYYY HH:MM AM/PM: {formatted_date}")
    except ValueError as e:
        print(f"Error processing date: {e}")