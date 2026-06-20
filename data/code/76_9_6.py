from datetime import datetime

def days_between(start_date: str, end_date: str) -> int:
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    return (end - start).days

if __name__ == '__main__':
    print(days_between('2023-01-01', '2023-01-31'))