from datetime import datetime

def convert_date(date_str):
    return datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_dates = ['01/23/2020', '12/31/2021', '07/04/2022']
    converted_dates = [convert_date(date) for date in sample_dates]
    print(converted_dates)