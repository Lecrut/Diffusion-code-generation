def is_zero(value):
    try:
        return value == 0
    except TypeError:
        return False

if __name__ == '__main__':
    test_values = [1, 0, -1, "0", None, [], {}, lambda: 0]
    for val in test_values:
        print(f"is_zero({val!r}) -> {is_zero(val)}")