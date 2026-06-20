def compare_dates(date1, date2):
    if date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    date1 = datetime.date(2023, 4, 15)
    date2 = datetime.date(2023, 4, 10)
    print(compare_dates(date1, date2))