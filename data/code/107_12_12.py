from datetime import datetime

def convert_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%d-%b-%Y')
    return date_obj.strftime('%Y%m%d')
if __name__ == '__main__':
    sample_date = '15-Jan-2023'
    converted_date = convert_date_format(sample_date)
    print(converted_date)