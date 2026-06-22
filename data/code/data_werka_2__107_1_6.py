from datetime import datetime

def convert_date(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    parts = date_string.split('/')
    if len(parts) != 3:
        raise ValueError("Invalid date format")
    month, day, year = parts
    try:
        dt = datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        raise ValueError(f"Invalid date: {date_string}")
    return dt.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '03/15/2024'
    result = convert_date(sample_date)
    print(result)