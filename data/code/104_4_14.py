def are_dates_equal(date_tuple1, date_tuple2):
    if not (isinstance(date_tuple1, tuple) and isinstance(date_tuple2, tuple)):
        raise TypeError("Both inputs must be tuples.")
    if len(date_tuple1) != 3 or len(date_tuple2) != 3:
        raise ValueError("Each tuple must contain exactly three elements.")
    try:
        year1, month1, day1 = date_tuple1
        year2, month2, day2 = date_tuple2
        return year1 == year2 and month1 == month2 and day1 == day2
    except TypeError:
        raise ValueError("All tuple elements must be integers.")

if __name__ == '__main__':
    date_input1 = (2023, 10, 25)
    date_input2 = (2023, 10, 25)
    try:
        result = are_dates_equal(date_input1, date_input2)
        print(result)
    except ValueError as e:
        print(e)