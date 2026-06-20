from datetime import datetime

def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        return date_object.strftime('%d-%m-%Y')
    except ValueError:
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.")

if __name__ == '__main__':
    sample_date = '12/31/2023'
    try:
        converted_date = convert_date_format(sample_date)
        print(converted_date)
    except ValueError as e:
        print(e)