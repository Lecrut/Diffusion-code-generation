from datetime import datetime

def days_between(start_date_str, end_date_str):
    start_date = datetime.fromisoformat(start_date_str)
    end_date = datetime.fromisoformat(end_date_str)
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    print(days_between('2023-01-01', '2023-01-31'))