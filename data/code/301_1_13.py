from datetime import datetime

def convert_date(date_str):
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    return date_obj.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_dates = ['04/15/2023', '11/27/2022', '06/30/2021']
    formatted_dates = [convert_date(date) for date in sample_dates]
    print(formatted_dates)