from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    return date_obj.strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_dates = ['01/01/2023', '05/15/2024', '12/31/1999']
    formatted_dates = [convert_date_format(date) for date in sample_dates]
    print(formatted_dates)