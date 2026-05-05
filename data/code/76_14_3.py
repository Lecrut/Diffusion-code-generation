import datetime
if __name__ == '__main__':
    date1 = datetime.date(2023, 1, 1)
    date2 = datetime.date(2023, 1, 31)
    difference = (date2 - date1).days
    print(difference)