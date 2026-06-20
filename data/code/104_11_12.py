import datetime

def calculate_day_difference(date1, date2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    sample_date1 = datetime.datetime(2023, 10, 26, 10, 30, 0)
    sample_date2 = datetime.datetime(2024, 1, 5, 15, 45, 0)
    print(calculate_day_difference(sample_date1, sample_date2))