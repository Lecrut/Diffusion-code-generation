from datetime import datetime

def validate_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def convert_date_format(date_string):
    if validate_date_format(date_string):
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        return date_object.strftime('%d-%m-%Y')
    else:
        raise ValueError("Invalid date format")

if __name__ == '__main__':
    sample_date = '12/31/2023'
    converted_date = convert_date_format(sample_date)
    print(converted_date)