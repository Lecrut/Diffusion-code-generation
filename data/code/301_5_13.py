from datetime import datetime

def convert_date_format(date_str):
    dt = datetime.strptime(date_str, '%d/%m/%Y %I:%M %p')
    return dt.strftime('%Y-%m-%dT%H:%M:00')

if __name__ == '__main__':
    sample_date = '15/08/2023 09:45 AM'
    print(convert_date_format(sample_date))