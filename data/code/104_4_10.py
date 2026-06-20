def are_dates_equal(date1, date2):
    return date1 == date2

if __name__ == '__main__':
    date_tuple1 = (2023, 10, 25)
    date_tuple2 = (2023, 10, 25)
    result = are_dates_equal(date_tuple1, date_tuple2)
    print(result)