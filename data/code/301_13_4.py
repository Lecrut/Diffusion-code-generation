from datetime import datetime

def convert_date_format(iso_date):
    return datetime.strptime(iso_date, '%Y-%m-%d').strftime('%d %B %Y')

if __name__ == '__main__':
    sample_date = '2021-01-01'
    print(convert_date_format(sample_date))