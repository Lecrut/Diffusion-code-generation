def are_dates_equal(date1: tuple[int, int, int], date2: tuple[int, int, int]) -> bool:
    return date1 == date2
if __name__ == '__main__':
    date_a = (2023, 10, 25)
    date_b = (2023, 10, 25)
    result = are_dates_equal(date_a, date_b)
    print(result)