from datetime import date

def check_date_equality(d1, d2):
    return d1 == d2
if __name__ == '__main__':
    sample_date1 = date(2023, 11, 5)
    sample_date2 = date(2023, 11, 5)
    sample_date3 = date(2023, 11, 6)
    result1 = check_date_equality(sample_date1, sample_date2)
    result2 = check_date_equality(sample_date1, sample_date3)
    print(result1)
    print(result2)