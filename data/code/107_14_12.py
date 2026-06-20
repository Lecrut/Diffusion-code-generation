from datetime import datetime

def is_valid_date(date_str, fmt):
    try:
        datetime.strptime(date_str, fmt)
        return True
    except ValueError:
        return False

def convert_to_iso_format(date_str):
    input_formats = ['%d-%m-%Y %H:%M:%S']
    for fmt in input_formats:
        if is_valid_date(date_str, fmt):
            dt_object = datetime.strptime(date_str, fmt)
            return dt_object.strftime('%Y-%m-%dT%H:%M:%S')
    raise ValueError("Date format not recognized")

if __name__ == '__main__':
    date1 = '31-12-2023 23:59:59'
    print(f"Input: {date1}, ISO Format: {convert_to_iso_format(date1)}")