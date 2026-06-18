def evaluate_conditions(value):
    if value > 10:
        print("Value is large.")
    elif value < -5:
        print("Value is negative and small.")
    else:
        print("Value is within normal range.")
if __name__ == '__main__':
    test_value = 3.7
    evaluate_conditions(test_value)