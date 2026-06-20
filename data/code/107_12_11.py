from datetime import datetime

DATE_FORMAT_INPUT = '%d-%b-%Y'
DATE_FORMAT_OUTPUT = '%Y%m%d'

def convert_date_string(date_string):
    try:
        date_obj = datetime.strptime(date_string, DATE_FORMAT_INPUT)
        return date_obj.strftime(DATE_FORMAT_OUTPUT)
    except ValueError:
        return "Invalid Date Format"

if __name__ == '__main__':
    sample_date1 = '25-Jan-2023'
    sample_date2 = '01-Feb-2024'
    sample_date3 = '15-Mar-2023'
    sample_date4 = 'not-a-date'

    print(f"'{sample_date1}' converted: {convert_date_string(sample_date1)}")
    print(f"'{sample_date2}' converted: {convert_date_string(sample_date2)}")
    print(f"'{sample_date3}' converted: {convert_date_string(sample_date3)}")
    print(f"'{sample_date4}' converted: {convert_date_string(sample_date4)}")