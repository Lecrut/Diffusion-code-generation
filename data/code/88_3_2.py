def check_conditions_met(a: bool, b: bool) -> bool:
    return a and b

if __name__ == '__main__':
    conditions = {
        (True, True): "Both are true",
        (False, True): "First is false",
        (True, False): "Second is false",
        (False, False): "Both are false"
    }
    for inputs, expected in conditions.items():
        result = check_conditions_met(*inputs)
        print(f"Input: {inputs}, Expected: {expected}, Got: {'Both are true' if result else 'At least one is false'}")