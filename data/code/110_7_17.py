import datetime

def sort_dates(date_strings):
    DATE_FORMAT = '%m-%d-%Y'
    parsed_dates = [datetime.datetime.strptime(date_str, DATE_FORMAT) for date_str in date_strings]
    parsed_dates.sort()
    sorted_date_strings = [parsed_date.strftime(DATE_FORMAT) for parsed_date in parsed_dates]
    return sorted_date_strings

if __name__ == '__main__':
    sample_dates = ['12-31-2020', '01-01-2021', '11-25-2021']
    print(sort_dates(sample_dates))