def evaluate_conditions(value):
    if value > 10:
        print("Value is greater than ten.")
    elif value < -5:
        print("Value is less than negative five.")
    else:
        print("Value falls within the expected range.")
if __name__ == '__main__':
    sample_value = 7.5
    evaluate_conditions(sample_value)