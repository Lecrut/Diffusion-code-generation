from datetime import datetime

def convert_date(date_str):
    return datetime.strptime(date_str, '%d/%m/%Y %I:%M %p').strftime('%Y-%m-%dT%H:%M:00')

if __name__ == '__main__':
    sample_date = '15/08/2023 04:30 PM'
    print(convert_date(sample_date))