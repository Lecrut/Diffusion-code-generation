def change_ratio(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == 'add_to_one':
        return (a + 1) / b
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Simple Multiplication ---")
    ratio_a1 = 10
    ratio_b1 = 2
    result1 = change_ratio(ratio_a1, ratio_b1, 'multiply')
    print(f"Original Ratio: {ratio_a1}:{ratio_b1}")
    print(f"Result (Multiplied): {result1}")
    print("-" * 30)
    print("--- Scenario 2: Simple Division ---")
    ratio_a2 = 15
    ratio_b2 = 3
    result2 = change_ratio(ratio_a2, ratio_b2, 'divide')
    print(f"Original Ratio: {ratio_a2}:{ratio_b2}")
    print(f"Result (Divided): {result2}")
    print("-" * 30)
    print("--- Scenario 3: Adding One to the First Term ---")
    ratio_a3 = 10
    ratio_b3 = 4
    result3 = change_ratio(ratio_a3, ratio_b3, 'add_to_one')
    print(f"Original Ratio: {ratio_a3}:{ratio_b3}")
    print(f"Result (A+1)/(B): {result3}")
    print("-" * 30)