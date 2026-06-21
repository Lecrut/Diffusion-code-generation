def check_any_true(values):
    found = False
    index = 0
    length = len(values)
    while index < length:
        if values[index]:
            found = True
            break
        index += 1
    return found

if __name__ == '__main__':
    test_cases = [False, True, False, False, True, False]
    outcome = check_any_true(test_cases)
    print(outcome)