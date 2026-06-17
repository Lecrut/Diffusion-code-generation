def change_ratio(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == 'add_to_ratio':
        k = 5
        return a + k, b + k
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Multiplying the Ratio ---")
    ratio_a1 = 2
    ratio_b1 = 3
    result1 = change_ratio(ratio_a1, ratio_b1, 'multiply')
    print(f"Original Ratio: {ratio_a1}:{ratio_b1}")
    print(f"Result (Multiplied): {result1}")
    print("\n--- Scenario 2: Dividing the Ratio ---")
    ratio_a2 = 10
    ratio_b2 = 4
    result2 = change_ratio(ratio_a2, ratio_b2, 'divide')
    print(f"Original Ratio: {ratio_a2}:{ratio_b2}")
    print(f"Result (Divided): {result2}")
    print("\n--- Scenario 3: Adding a Constant to Both Parts of the Ratio ---")
    ratio_a3 = 7
    ratio_b3 = 11
    result3 = change_ratio(ratio_a3, ratio_b3, 'add_to_ratio')
    print(f"Original Ratio: {ratio_a3}:{ratio_b3}")
    print(f"Result (Added 5): {result3}")