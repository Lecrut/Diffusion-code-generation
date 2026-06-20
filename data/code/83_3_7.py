from datetime import date

def are_dates_equal(d1, d2):
    return d1 == d2

if __name__ == '__main__':
    d1 = date(2023, 10, 5)
    d2 = date(2023, 10, 5)
    print(are_dates_equal(d1, d2))