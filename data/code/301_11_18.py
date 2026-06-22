from datetime import datetime

DATE_FORMAT_INPUT = '%m/%d/%Y'
DATE_FORMAT_OUTPUT = '%Y-%m-%d'

def convert_date_format(date_list):
    return [datetime.strptime(date, DATE_FORMAT_INPUT).strftime(DATE_FORMAT_OUTPUT) for date in date_list]

if __name__ == '__main__':
    sample_dates = ['01/01/2023', '12/31/2022']
    formatted_dates = convert_date_format(sample_dates)
    print(formatted_dates)