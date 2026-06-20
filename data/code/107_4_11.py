from datetime import datetime

DATE_FORMAT_INPUT = '%d.%m.%Y'
DATE_FORMAT_OUTPUT = '%Y-%m-%d'

def reformat_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, DATE_FORMAT_INPUT)
        return date_obj.strftime(DATE_FORMAT_OUTPUT)
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    test_dates = ['12.05.2023', '01.01.2020', '31.12.2022']
    for date in test_dates:
        print(reformat_date(date))