def evaluate_conditions(value):
    if value > 10:
        print("Value is greater than ten")
    elif value == 5:
        print("Value equals five")
    else:
        print("Value does not meet specific criteria")
if __name__ == '__main__':
    test_value = 7
    evaluate_conditions(test_value)