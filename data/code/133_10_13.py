def validate_input(data):
    if not all(isinstance(item, bool) for item in data):
        raise ValueError("All items in the input list must be boolean values.")

def evaluate_logic(data):
    validate_input(data)
    return any(item for item in data)

if __name__ == '__main__':
    sample_data = [True, False, True]
    result = evaluate_logic(sample_data)
    print(result)