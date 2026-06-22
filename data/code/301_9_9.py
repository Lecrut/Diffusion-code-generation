from datetime import datetime

def convert_date_format(date_str):
    dt = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f%z')
    return dt.strftime('%d-%b-%Y %I:%M %p')

if __name__ == '__main__':
    sample_date = '2023-10-05T14:30:45.678901+08:00'
    print(convert_date_format(sample_date))