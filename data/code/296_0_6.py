def change_ratio(a, b, operation):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == "add_to_a":
        return (a + b) / b
    elif operation == "subtract_from_b":
        return a / (b - a)
    else:
        return "Invalid operation"
if __name__ == '__main__':
    ratio_a = 10
    ratio_b = 5
    print(f"Original Ratio: {ratio_a}:{ratio_b}")
    result1 = change_ratio(ratio_a, ratio_b, "multiply")
    print(f"Scenario 1 (Multiply): New Ratio Components = {result1}:1")
    result2 = change_ratio(ratio_a, ratio_b, "divide")
    print(f"Scenario 2 (Divide B by A): New Ratio Value = {result2}")
    result3 = change_ratio(ratio_a, ratio_b, "add_to_a")
    print(f"Scenario 3 (Add to A and Divide by B): New Ratio Value = {result3}")
    result4 = change_ratio(ratio_a, ratio_b, "subtract_from_b")
    print(f"Scenario 4 (Subtract from B and Divide by A): New Ratio Value = {result4}")