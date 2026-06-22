from datetime import date

def compare_dates(tuple_a, tuple_b):
    year_a, month_a, day_a = tuple_a
    year_b, month_b, day_b = tuple_b
    object_a = date(year_a, month_a, day_a)
    object_b = date(year_b, month_b, day_b)
    return object_a == object_b

if __name__ == '__main__':
    first_date = (2025, 1, 1)
    second_date = (2025, 1, 1)
    check_result = compare_dates(first_date, second_date)
    print(check_result)