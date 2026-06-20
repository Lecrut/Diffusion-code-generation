from datetime import datetime

def convert_date_format(date_string):
    try:
        date_object = datetime.strptime(date_string, '%m/%d/%Y')
        return date_object.strftime('%d-%m-%Y')
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date = '12/31/2023'
    print(convert_date_format(sample_date))