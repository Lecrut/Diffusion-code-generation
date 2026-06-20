import datetime

def next_month(start_date):
    return start_date.replace(day=28) + datetime.timedelta(days=4)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 11, 15)
    print(next_month(sample_date))