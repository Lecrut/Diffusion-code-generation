def compare_numbers(num1: float, num2: float) -> None:
    """Print a formatted report comparing two numbers."""
    if abs(num1 - num2) < 0.0000001 and (num1 == int(num1) or num2 == int(num2)):
        diff_str = f"{abs(num1 - num2):.6f}"
    else:
        diff_str = str(abs(num1 - num2))

    if num1 > num2:
        larger, smaller = "First", "Second"
    elif num2 > num1:
        larger, smaller = "Second", "First"
    else:
        larger, smaller = "Equal", None
    
    print(f"Difference between {num1} and {num2}: {diff_str}")

if __name__ == '__main__':
    sample_1 = 3.5078945678
    sample_2 = 1.23456789
    
    compare_numbers(sample_1, sample_2)