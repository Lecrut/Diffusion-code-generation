def change_ratio(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == 'add_to_ratio':
        new_a = a + b
        new_b = b
        return new_a, new_b
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Multiplying the Ratio ---")
    ratio_a1 = 2
    ratio_b1 = 5
    operation1 = 'multiply'
    result1 = change_ratio(ratio_a1, ratio_b1, operation1)
    print(f"Original Ratio: {ratio_a1}:{ratio_b1}")
    print(f"Operation: {operation1}")
    print(f"New Ratio (Product): {result1}")
    print("-" * 30)
    print("--- Scenario 2: Dividing the Ratio ---")
    ratio_a2 = 10
    ratio_b2 = 4
    operation2 = 'divide'
    result2 = change_ratio(ratio_a2, ratio_b2, operation2)
    print(f"Original Ratio: {ratio_a2}:{ratio_b2}")
    print(f"Operation: {operation2}")
    print(f"New Ratio (Quotient): {result2}")
    print("-" * 30)
    print("--- Scenario 3: Adding a Value to One Part of the Ratio ---")
    ratio_a3 = 3
    ratio_b3 = 7
    operation3 = 'add_to_ratio'
    result3_a, result3_b = change_ratio(ratio_a3, ratio_b3, operation3)
    print(f"Original Ratio: {ratio_a3}:{ratio_b3}")
    print(f"Operation: {operation3} (Adding to the first part)")
    print(f"New Ratio: {result3_a}:{result3_b}")
    print("-" * 30)