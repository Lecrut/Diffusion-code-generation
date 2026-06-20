from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def convert_date_format(date_string):
    if not is_valid_date(date_string):
        raise ValueError("Invalid date format")
    date_object = datetime.strptime(date_string, '%m/%d/%Y')
    return date_object.strftime('%d-%m-%Y')

if __name__ == '__main__':
    sample_date = '12/31/2023'
    print(convert_date_format(sample_date))