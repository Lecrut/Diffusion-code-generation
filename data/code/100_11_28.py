def all_booleans_identical(data):
    if len(data) <= 1:
        return True
    reference = data[0]
    index = 1
    length = len(data)
    while index < length:
        current = data[index]
        if current != reference:
            return False
        index += 1
    return True

if __name__ == '__main__':
    test_values = [False, False, False]
    outcome = all_booleans_identical(test_values)
    print(outcome)