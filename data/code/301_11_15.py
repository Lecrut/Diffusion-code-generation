from datetime import datetime

def convert_date_format(dates):
    return [datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d') for date in dates]

if __name__ == '__main__':
    sample_dates = ['12/31/2020', '01/01/2021', '07/4/2022']
    print(convert_date_format(sample_dates))