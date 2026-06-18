def compare_numbers(num1: float, num2: float) -> str:
    """Compare two numbers and return a formatted report of their difference."""
    diff = num1 - num2
    
    if abs(diff) < 0.0001: 
        result_msg = f"{num1} is equal to {num2}"
    elif num1 > num2: 
        result_msg = f"{num1} is larger than {num2}"
    else: 
        result_msg = f"{num2} is larger than {num1}"
    
    return (f"Comparison Report:\nDifference ({num2} - {num1}): {-diff:.4f}\n{result_msg}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    value_a = 10.5
    value_b = 7.3
    
    report = compare_numbers(value_a, value_b)
    print(report)