import datetime
def date_difference(date1, date2):
    if date1 > date2:
        return date1 - date2
    else:
        return date2 - date1
if __name__ == '__main__':
    date_a = datetime.datetime(2023, 10, 29, 10, 0, 0)
    date_b = datetime.datetime(2023, 11, 2, 15, 30, 0)
    difference = date_difference(date_a, date_b)
    print(difference)