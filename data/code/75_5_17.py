import datetime
DAYS_IN_YEAR = 365

def calculate_date_difference(date1, date2):
    delta = abs(date2 - date1)
    return delta.days
if __name__ == '__main__':
    sample_date1 = datetime.date(2022, 1, 1)
    sample_date2 = datetime.date(2023, 1, 1)
    result = calculate_date_difference(sample_date1, sample_date2)
    print(result)