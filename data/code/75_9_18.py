from datetime import date

def date_difference_days(date1, date2):
    delta = abs(date2 - date1)
    return delta.days
if __name__ == '__main__':
    sample_date1 = date(2023, 10, 26)
    sample_date2 = date(2023, 11, 26)
    result = date_difference_days(sample_date1, sample_date2)
    print(result)