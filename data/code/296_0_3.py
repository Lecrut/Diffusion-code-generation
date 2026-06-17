def change_ratio(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == 'add_to_ratio':
        return (a + 5) / b
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Simple Multiplication ---")
    ratio_a1 = 10
    ratio_b1 = 4
    result1 = change_ratio(ratio_a1, ratio_b1, 'multiply')
    print(f"Original Ratio: {ratio_a1}:{ratio_b1}")
    print(f"Result after multiplication: {result1}")
    print("-" * 30)
    print("--- Scenario 2: Simple Division ---")
    ratio_a2 = 20
    ratio_b2 = 5
    result2 = change_ratio(ratio_a2, ratio_b2, 'divide')
    print(f"Original Ratio: {ratio_a2}:{ratio_b2}")
    print(f"Result after division: {result2}")
    print("-" * 30)
    print("--- Scenario 3: Changing the Ratio by Adding a Constant (e.g., adding 5 to the first part) ---")
    ratio_a3 = 10
    ratio_b3 = 4
    result3 = change_ratio(ratio_a3, ratio_b3, 'add_to_ratio')
    print(f"Original Ratio: {ratio_a3}:{ratio_b3}")
    print(f"Result after adding 5 to the first part (new ratio): {result3}")
    print("-" * 30)