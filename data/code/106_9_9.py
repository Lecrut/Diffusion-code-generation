import datetime

def calculate_year_difference(date1, date2):
    delta = abs(date2 - date1)
    return delta.days // 365

if __name__ == '__main__':
    sample_date1 = datetime.date(2000, 1, 1)
    sample_date2 = datetime.date(2020, 1, 1)
    print(calculate_year_difference(sample_date1, sample_date2))