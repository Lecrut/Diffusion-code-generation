from datetime import datetime

def convert_date_format(dates):
    return [datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d') for date in dates]

if __name__ == '__main__':
    sample_dates = ['01/01/2023', '12/31/2022', '07/04/2021']
    formatted_dates = convert_date_format(sample_dates)
    print(formatted_dates)