from datetime import datetime

def validate_date_format(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def convert_date_format(date_str):
    if not validate_date_format(date_str):
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    return date_str.replace('-', '/')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    converted_date = convert_date_format(sample_date)
    print(converted_date)