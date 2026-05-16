from datetime import date
if __name__ == '__main__':
    date1 = date(2023, 1, 31)
    date2 = date(2023, 1, 1)
    difference = abs(date1 - date2).days
    print(difference)