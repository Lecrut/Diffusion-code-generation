from datetime import datetime

def convert_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%d %B %Y')

if __name__ == '__main__':
    sample_date = '2021-01-01'
    print(convert_date(sample_date))