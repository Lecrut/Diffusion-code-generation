from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    return date_obj.strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_dates = ['12/31/2022', '01/01/2023']
    for date in sample_dates:
        converted_date = convert_date_format(date)
        print(f"Original: {date}, Converted: {converted_date}")