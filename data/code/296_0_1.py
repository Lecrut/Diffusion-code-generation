def change_ratio(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == 'add_to_ratio':
        if b != 0:
            return (a / b) + b
        else:
            return "Error: Division by zero in addition"
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Multiplying the Ratio Components ---")
    ratio_a1 = 10
    ratio_b1 = 4
    result1 = change_ratio(ratio_a1, ratio_b1, 'multiply')
    print(f"Original Ratio: {ratio_a1}:{ratio_b1}")
    print(f"Result (Multiplied): {result1}")
    print("-" * 30)
    print("--- Scenario 2: Dividing the Ratio Components ---")
    ratio_a2 = 20
    ratio_b2 = 5
    result2 = change_ratio(ratio_a2, ratio_b2, 'divide')
    print(f"Original Ratio: {ratio_a2}:{ratio_b2}")
    print(f"Result (Divided): {result2}")
    print("-" * 30)
    print("--- Scenario 3: Adding a Constant to the Ratio Value ---")
    ratio_a3 = 12
    ratio_b3 = 3
    constant_c = 5
    result3 = change_ratio(ratio_a3, ratio_b3, 'add_to_ratio')
    print(f"Original Ratio: {ratio_a3}:{ratio_b3}")
    print(f"Result (Ratio + Constant): {result3} (Calculated as ({ratio_a3}/{ratio_b3}) + {ratio_b3})")
    print("-" * 30)