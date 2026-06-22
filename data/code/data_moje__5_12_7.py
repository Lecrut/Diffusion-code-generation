def compare_lengths_meters_to_cm(a, b):
    a_cm = a * 100
    b_cm = b * 100
    if a_cm >= b_cm:
        return a
    else:
        return b

if __name__ == '__main__':
    result = compare_lengths_meters_to_cm(1.5, 2.0)
    print(result)