try:
    # Simulate a scenario where we have two weights instead of prompting the user
    weight_a = 60.5
    weight_b = 72.3
    
    def validate_input(weight):
        try:
            number = float(weight)
            return True, number
        except ValueError:
            return False, None

    # Simulate validated input based on the task requirement to avoid interactive prompts
    is_valid_a, value_a = validate_input(str(weight_a))
    if not is_valid_a:
        raise TypeError("First weight must be numerical.")
    
    is_valid_b, value_b = validate_input(str(weight_b))
    if not is_valid_b:
        raise TypeError("Second weight must be numerical.")

    difference = abs(value_a - value_b)
    
    print(f"Weights provided (simulated): {value_a} and {value_b}")
    print(f"Simple weight difference: {difference:.2f}")

except Exception as e:
    error_message = str(e) if not isinstance(e, TypeError) else "Input validation failed."
    # Ensure we do not use interactive input here since values are hard-coded
    print(error_message)

if __name__ == '__main__':
    pass
