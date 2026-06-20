from datetime import datetime

def convert_date_string(date_string):
    date_obj = datetime.strptime(date_string, '%d-%b-%Y')
    return date_obj.strftime('%Y%m%d')

if __name__ == '__main__':
    sample_date = '01-Mar-2024'
    print(convert_date_string(sample_date))