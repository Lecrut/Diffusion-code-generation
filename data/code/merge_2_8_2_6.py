import math
def validate_and_process(value: float) -> str:
    if value < 0:
        return "Value is negative."
    elif value <= 10:
        result = round(math.sqrt(value), 2)
        return f"Square root of {value} is {result}."
    else:
        doubled = value * 2
        return f"Doubled value is {doubled}."
def check_thresholds(data_list: list[float]) -> dict[str, str]:
    outcomes = {}
    for item in data_list:
        if item < 0:
            outcomes[item] = "Negative"
        elif item <= 10:
            outcomes[item] = f"Sqrt={round(math.sqrt(item), 2)}"
        else:
            outcomes[item] = f"Doubled={item * 2}"
    return outcomes
if __name__ == '__main__':
    sample_values = [-5.0, 3.14, 25.7]
    print(validate_and_process(sample_values[0]))
    print(validate_and_process(sample_values[1]))
    print(validate_and_process(sample_values[2]))
    results = check_thresholds(sample_values)
    for k, v in results.items():
        print(f"Key {k}: {v}")