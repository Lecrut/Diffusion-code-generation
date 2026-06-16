def evaluate_conditions(value: int) -> None:
    if value == 10:
        print("Condition met: Value is ten.")
    elif value > 20:
        print("Condition met: Value exceeds twenty.")
    else:
        print("No specific condition was met for this value.")
if __name__ == '__main__':
    sample_value = 15
    evaluate_conditions(sample_value)