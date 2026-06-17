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
            return "Error: Division by zero in addition scenario"
    else:
        return "Invalid operation"
if __name__ == '__main__':
    print("--- Scenario 1: Simple Multiplication ---")
    ratio_a1 = 10
    ratio_b1 = 4
    result1 = change_ratio(ratio_a1, ratio_b1, 'multiply')
    print(f"Original Ratio components: {ratio_a1} and {ratio_b1}")
    print(f"Result of multiplication: {result1}\n")
    print("--- Scenario 2: Simple Division ---")
    ratio_a2 = 20
    ratio_b2 = 5
    result2 = change_ratio(ratio_a2, ratio_b2, 'divide')
    print(f"Original Ratio components: {ratio_a2} and {ratio_b2}")
    print(f"Result of division (A/B): {result2}\n")
    print("--- Scenario 3: Changing Ratio by Adding a Constant ---")
    ratio_a3 = 10
    ratio_b3 = 3
    constant_c3 = 5
    result3 = change_ratio(ratio_a3, ratio_b3, 'add_to_ratio')
    print(f"Original Ratio components: {ratio_a3} and {ratio_b3}")
    print(f"Result of (A/B) + B: {result3}\n")