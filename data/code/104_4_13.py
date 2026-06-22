def compare_dates(date_tuple_1, date_tuple_2):
    y1, m1, d1 = date_tuple_1
    y2, m2, d2 = date_tuple_2
    if y1 != y2:
        return False
    if m1 != m2:
        return False
    return d1 == d2

if __name__ == '__main__':
    t1 = (2024, 1, 1)
    t2 = (2024, 1, 1)
    print(compare_dates(t1, t2))