from datetime import datetime

def convert_dates(date_list):
    return [datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d') for date in date_list]

if __name__ == '__main__':
    sample_dates = ['01/01/2023', '12/31/2023', '07/4/2022']
    formatted_dates = convert_dates(sample_dates)
    print(formatted_dates)