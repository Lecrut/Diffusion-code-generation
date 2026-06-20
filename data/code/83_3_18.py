from datetime import date

def are_dates_equal(d1, d2):
    return d1 == d2

if __name__ == '__main__':
    d1 = date(2023, 4, 1)
    d2 = date(2023, 4, 1)
    print(are_dates_equal(d1, d2))