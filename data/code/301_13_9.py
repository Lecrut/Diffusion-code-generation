from datetime import datetime

def convert_date_format(iso_date):
    return datetime.strptime(iso_date, '%Y-%m-%d').strftime('%d %B %Y')

if __name__ == '__main__':
    print(convert_date_format('2021-01-01'))