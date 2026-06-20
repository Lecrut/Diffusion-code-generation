def is_same_date(date1, date2):
    return date1 == date2
if __name__ == '__main__':
    print(is_same_date((2023, 4, 15), (2023, 4, 15)))
    print(is_same_date((2023, 4, 15), (2023, 4, 16)))