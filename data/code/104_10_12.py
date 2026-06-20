def compare_dates(date1, date2):
    if date1 > date2:
        return 1
    elif date1 < date2:
        return -1
    else:
        return 0
if __name__ == '__main__':
    print(compare_dates(datetime.date(2023, 4, 5), datetime.date(2023, 4, 4)))
    print(compare_dates(datetime.date(2023, 4, 4), datetime.date(2023, 4, 5)))
    print(compare_dates(datetime.date(2023, 4, 4), datetime.date(2023, 4, 4)))