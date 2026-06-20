import datetime

def date_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = datetime.date(2023, 1, 1)
    sample_date2 = datetime.date(2023, 1, 15)
    print(date_difference(sample_date1, sample_date2))