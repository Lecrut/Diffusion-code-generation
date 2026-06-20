from datetime import datetime
DATE_FORMAT_INPUT = '%d-%b-%Y'
DATE_FORMAT_OUTPUT = '%Y%m%d'

def convert_date_string(date_string):
    try:
        date_obj = datetime.strptime(date_string, DATE_FORMAT_INPUT)
        return date_obj.strftime(DATE_FORMAT_OUTPUT)
    except ValueError:
        raise ValueError('Invalid Date Format')
if __name__ == '__main__':
    sample_date = '25-Jan-2023'
    print(convert_date_string(sample_date))