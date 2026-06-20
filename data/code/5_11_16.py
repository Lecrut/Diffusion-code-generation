def compare_measurements(first, second):
    difference = first - second
    ratio = first / second if second != 0 else None
    is_greater = first > second
    return difference, ratio, is_greater

if __name__ == '__main__':
    val_a = 10.5
    val_b = 3.2
    result = compare_measurements(val_a, val_b)
    print(result)