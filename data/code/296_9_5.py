def calculate_ratio_transformation(start_ratio, operation, value):
    if operation == "add":
        return start_ratio + value
    elif operation == "subtract":
        return start_ratio - value
    elif operation == "multiply":
        return start_ratio * value
    elif operation == "divide":
        if value != 0:
            return start_ratio / value
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
if __name__ == '__main__':
    start_ratio = 5
    operation = "multiply"
    value = 3
    final_ratio = calculate_ratio_transformation(start_ratio, operation, value)
    print(f"Starting Ratio: {start_ratio}")
    print(f"Operation: {operation}, Value: {value}")
    print(f"Final Transformed Ratio: {final_ratio}")