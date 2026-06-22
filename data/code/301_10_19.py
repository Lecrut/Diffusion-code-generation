import datetime

def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def convert_date_format(date_string):
    if not is_valid_date(date_string):
        return "Error: Invalid date format. Please use YYYY-MM-DD."
    return datetime.datetime.strptime(date_string, '%Y-%m-%d').strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_date = "2023-10-27"
    converted_date = convert_date_format(sample_date)
    print(converted_date)