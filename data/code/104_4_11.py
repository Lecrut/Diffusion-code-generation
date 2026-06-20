def is_same_date(date_tuple1: tuple, date_tuple2: tuple) -> bool:
    return date_tuple1 == date_tuple2

if __name__ == '__main__':
    result = is_same_date((2023, 10, 25), (2023, 10, 25))
    print(result)