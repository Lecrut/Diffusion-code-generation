from datetime import datetime

def convert_dates(date_list):
    date_format = {'MM/DD/YYYY': '%m/%d/%Y', 'YYYY-MM-DD': '%Y-%m-%d'}
    return [datetime.strptime(date, date_format['MM/DD/YYYY']).strftime(date_format['YYYY-MM-DD']) for date in date_list]

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '01/01/2021', '07/4/2022']
    converted_dates = convert_dates(sample_dates)
    print(converted_dates)