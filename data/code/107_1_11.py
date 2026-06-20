from datetime import datetime

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def convert_date_format(date_string):
    if not is_valid_date(date_string):
        return "Invalid date format"
    date_object = datetime.strptime(date_string, '%m/%d/%Y')
    iso_format = date_object.strftime('%d-%m-%Y')
    return iso_format

if __name__ == '__main__':
    sample_date = '12/31/2023'
    print(convert_date_format(sample_date))