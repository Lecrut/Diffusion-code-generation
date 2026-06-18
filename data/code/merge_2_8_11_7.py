def evaluate_conditions(value):
    if value > 10:
        print("Value is greater than ten.")
    elif value == 5:
        print("Value equals five.")
    else:
        print("Condition not met.")
if __name__ == '__main__':
    sample_value = 7
    evaluate_conditions(sample_value)