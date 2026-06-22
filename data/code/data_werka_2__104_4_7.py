from datetime import date

def same_date(d1, d2):
    return date(*d1) == date(*d2)

if __name__ == '__main__':
    print(same_date((2023, 10, 5), (2023, 10, 5)))
    print(same_date((2023, 10, 5), (2023, 10, 6)))