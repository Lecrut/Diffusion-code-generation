from datetime import datetime
DATE_FORMAT = '%d/%m/%Y'

def sort_dates(date_strings):
    parsed_dates = [datetime.strptime(date_str, DATE_FORMAT) for date_str in date_strings]
    parsed_dates.sort()
    return [date.strftime(DATE_FORMAT) for date in parsed_dates]
if __name__ == '__main__':
    sample_dates = ['20/11/2023', '05/12/2023', '10/10/2023', '15/09/2023']
    sorted_dates = sort_dates(sample_dates)
    print(sorted_dates)