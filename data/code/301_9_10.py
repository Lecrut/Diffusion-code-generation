import datetime

def convert_date_format(date_str: str) -> str:
    date_formats = {
        'input': '%Y-%m-%dT%H:%M:%S.%f%z',
        'output': '%d-%b-%Y %I:%M %p'
    }
    try:
        dt_object = datetime.datetime.strptime(date_str, date_formats['input'])
        return dt_object.strftime(date_formats['output'])
    except ValueError as e:
        raise ValueError(f"Error parsing date '{date_str}': {e}")

if __name__ == '__main__':
    sample_date = "2023-10-27T14:30:45.678901+00:00"
    try:
        converted_date = convert_date_format(sample_date)
        print(f"Converted Date (DD-Mon-YYYY HH:MM AM/PM): {converted_date}")
    except ValueError as e:
        print(e)