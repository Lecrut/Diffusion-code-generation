def compare_numbers(num1: float, num2: float) -> None:
    """Compare two numbers and print a formatted report of their difference."""
    diff = abs(num1 - num2)
    
    if num1 > num2:
        larger_value = f"{num1:.4f}"
        smaller_value = f"{num2:.4f}"
        comparison_result = "The first number is larger."
    elif num2 > num1:
        larger_value = f"{num2:.4f}"
        smaller_value = f"{num1:.4f}"
        comparison_result = "The second number is larger."
    else:
        larger_value = f"{num1:.4f}"
        smaller_value = f"{num2:.4f}"
        comparison_result = "Both numbers are equal."

    print(f"Difference between the values: {diff:.4f}")
    print(f"Larger value: {larger_value}")
    print(smaller_value)
    print(comparison_result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or external dependencies.
    sample_num1 = 25.7394
    sample_num2 = 10.8625
    
    compare_numbers(sample_num1, sample_num2)