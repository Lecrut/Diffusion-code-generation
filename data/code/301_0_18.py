from datetime import datetime

def convert_date_format(date_str):
    return date_obj.strftime('%d/%m/%Y')

if __name__ == '__main__':
    sample_date = '2023-10-05'
    date_obj = datetime.strptime(sample_date, '%Y-%m-%d')
    print(convert_date_format(date_obj))