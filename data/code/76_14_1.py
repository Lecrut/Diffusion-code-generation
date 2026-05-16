from datetime import date
if __name__ == '__main__':
    d1 = date(2023, 1, 31)
    d2 = date(2023, 1, 1)
    difference = abs(d1 - d2).days
    print(difference)