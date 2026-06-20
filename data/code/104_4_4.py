def are_dates_equal(date1, date2):
    return date1 == date2
if __name__ == '__main__':
    print(are_dates_equal((2023, 4, 15), (2023, 4, 15)))
    print(are_dates_equal((2023, 4, 15), (2023, 4, 16)))