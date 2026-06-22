from datetime import datetime

def date_range(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    return (end - start).days

if __name__ == '__main__':
    print(date_range('2023-01-01', '2023-01-31'))