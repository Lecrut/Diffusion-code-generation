from datetime import datetime, timedelta

def next_month(date):
    return date.replace(day=28) + timedelta(days=4)

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 5)
    print(next_month(sample_date))