def compare_meters(m1, m2):
    if m1 > m2:
        return f"{m1} meters is longer than {m2} meters."
    elif m2 > m1:
        return f"{m2} meters is longer than {m1} meters."
    else:
        return f"{m1} meters and {m2} meters are equal."

if __name__ == '__main__':
    length_a = 5.2
    length_b = 3.7
    result = compare_meters(length_a, length_b)
    print(result)
    length_c = 8.0
    length_d = 8.0
    result2 = compare_meters(length_c, length_d)
    print(result2)