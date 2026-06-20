def are_both_true(val1, val2):
    return bool(val1) and bool(val2)

if __name__ == '__main__':
    test_values = [(True, True), (False, True), (True, False), (False, False)]
    for vals in test_values:
        result = are_both_true(vals[0], vals[1])
        print(f"are_both_true({vals[0]}, {vals[1]}) -> {result}")