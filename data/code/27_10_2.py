def check_difference(a, b):
    return a != b
if __name__ == '__main__':
    val1 = 10
    val2 = 10
    val3 = 5
    val4 = 15
    print(f"check_difference({val1}, {val2}): {check_difference(val1, val2)}")
    print(f"check_difference({val1}, {val3}): {check_difference(val1, val3)}")
    print(f"check_difference({val2}, {val4}): {check_difference(val2, val4)}")
    print(f"check_difference({val3}, {val4}): {check_difference(val3, val4)}")