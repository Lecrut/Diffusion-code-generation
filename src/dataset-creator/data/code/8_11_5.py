import sys
def evaluate_conditions(value: int) -> None:
    if value == 10:
        print("Value is ten.")
    elif value > 5 and value < 20:
        print("Value is between five and twenty.")
    else:
        print("No specific condition met.")
if __name__ == '__main__':
    sample_value = 15
    evaluate_conditions(sample_value)