from datetime import datetime

def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%d-%b-%Y')
        return date_obj.strftime('%Y%m%d')
    except ValueError:
        raise ValueError("Invalid Date Format")

if __name__ == '__main__':
    sample_date = '25-Jan-2023'
    print(convert_date_format(sample_date))