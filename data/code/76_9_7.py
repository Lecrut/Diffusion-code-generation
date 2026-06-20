from datetime import datetime

def days_between(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    return (end_date - start_date).days

if __name__ == '__main__':
    print(days_between('2023-01-01', '2023-12-31'))