from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    return date_obj.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_dates = ['09/15/2023', '11/20/2021', '04/07/2022']
    converted_dates = [convert_date_format(date) for date in sample_dates]
    print(converted_dates)