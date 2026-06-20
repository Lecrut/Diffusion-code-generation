def dates_match(date_tuple1, date_tuple2):
    return date_tuple1 == date_tuple2

if __name__ == '__main__':
    sample_date1 = (2023, 10, 25)
    sample_date2 = (2023, 10, 25)
    result = dates_match(sample_date1, sample_date2)
    print(result)