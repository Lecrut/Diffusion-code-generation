from datetime import datetime

def convert_date(date_string):
    if not isinstance(date_string, str):
        raise ValueError("Input must be a string")
    if len(date_string) != 10:
        raise ValueError("Invalid date format")
    if date_string[2] != '/' or date_string[5] != '/':
        raise ValueError("Invalid date format")
    try:
        dt = datetime.strptime(date_string, '%m/%d/%Y')
    except ValueError:
        raise ValueError(f"Invalid date: {date_string}")
    return dt.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '07/04/2024'
    result = convert_date(sample_date)
    print(result)