def are_dates_equal(date_tuple1, date_tuple2):
    return date_tuple1 == date_tuple2

if __name__ == '__main__':
    sample_date1 = (2023, 10, 25)
    sample_date2 = (2023, 10, 25)
    result = are_dates_equal(sample_date1, sample_date2)
    print(result)