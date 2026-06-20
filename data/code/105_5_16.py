from datetime import date, timedelta

def next_wednesday(start_date):
    days_until_wednesday = (2 - start_date.weekday()) % 7
    if days_until_wednesday == 0:
        days_until_wednesday += 7
    return start_date + timedelta(days=days_until_wednesday)

if __name__ == '__main__':
    sample_date = date(2023, 10, 10)
    print(next_wednesday(sample_date))