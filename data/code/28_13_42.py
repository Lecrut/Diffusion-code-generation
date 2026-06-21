def is_larger_than(first_number, second_number):
    if first_number > second_number:
        return True
    return False

if __name__ == '__main__':
    test_value_1 = 25
    test_value_2 = 10
    outcome = is_larger_than(test_value_1, test_value_2)
    print(outcome)