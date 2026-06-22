from datetime import date

def is_same_date(d1, d2):
    return date(d1[0], d1[1], d1[2]) == date(d2[0], d2[1], d2[2])

if __name__ == '__main__':
    print(is_same_date((2023, 10, 5), (2023, 10, 5)))
    print(is_same_date((2023, 10, 5), (2023, 10, 6)))