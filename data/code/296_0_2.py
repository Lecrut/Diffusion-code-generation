def change_ratio(a, b, operation):
    if operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == 'add_to_ratio':
        return (a + 1) / b
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Simple Multiplication ---")
    ratio_a1 = 2
    ratio_b1 = 5
    operation1 = 'multiply'
    result1 = change_ratio(ratio_a1, ratio_b1, operation1)
    print(f"Original Ratio: {ratio_a1}:{ratio_b1}")
    print(f"Operation: {operation1}")
    print(f"New Result: {result1}\n")
    print("--- Scenario 2: Simple Division ---")
    ratio_a2 = 10
    ratio_b2 = 4
    operation2 = 'divide'
    result2 = change_ratio(ratio_a2, ratio_b2, operation2)
    print(f"Original Ratio: {ratio_a2}:{ratio_b2}")
    print(f"Operation: {operation2}")
    print(f"New Result: {result2}\n")
    print("--- Scenario 3: Changing the Ratio by Adding to one part ---")
    ratio_a3 = 3
    ratio_b3 = 7
    operation3 = 'add_to_ratio'
    result3 = change_ratio(ratio_a3, ratio_b3, operation3)
    print(f"Original Ratio: {ratio_a3}:{ratio_b3}")
    print(f"Operation: {operation3} (Adding 1 to the first part)")
    print(f"New Result: {result3}\n")