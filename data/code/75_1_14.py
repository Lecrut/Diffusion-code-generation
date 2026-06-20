from datetime import datetime

def date_difference_days(date1, date2):
    delta = abs(date1 - date2)
    return delta.days

if __name__ == '__main__':
    sample_date1 = datetime(2023, 1, 1)
    sample_date2 = datetime(2023, 1, 15)
    print(date_difference_days(sample_date1, sample_date2))