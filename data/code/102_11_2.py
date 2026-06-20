from datetime import datetime

def is_weekday(date_str):
    return date_str.weekday() < 5

if __name__ == '__main__':
    sample_date = '2023-10-06'
    print(is_weekday(datetime.strptime(sample_date, '%Y-%m-%d')))