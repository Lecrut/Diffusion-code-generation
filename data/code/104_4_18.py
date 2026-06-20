def are_dates_equal(date1, date2):
    try:
        return date1 == date2
    except TypeError:
        raise ValueError("Both inputs must be tuples of (year, month, day).")

if __name__ == '__main__':
    sample_date1 = (2023, 10, 25)
    sample_date2 = (2023, 10, 25)
    try:
        result = are_dates_equal(sample_date1, sample_date2)
        print(result)
    except ValueError as e:
        print(e)