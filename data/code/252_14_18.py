def compare_numbers(num1, num2):
    if num1 > num2:
        return f"The first number ({num1}) is greater than the second number ({num2})."
    elif num1 < num2:
        return f"The first number ({num1}) is less than the second number ({num2})."
    else:
        return f"The first number ({num1}) is equal to the second number ({num2})."

def compare_two_simple_quantities_now_run_examples():
    examples = [
        (42, 100),
        (50, 50),
        (30, 75)
    ]
    for example in examples:
        result = compare_numbers(*example)
        print(result)

if __name__ == '__main__':
    sample_num1 = 42
    sample_num2 = 100
    print("--- Number Comparison ---")
    print(f"First quantity entered: {sample_num1}")
    print(f"Second quantity entered: {sample_num2}")
    compare_numbers(sample_num1, sample_num2)
    compare_two_simple_quantities_now_run_examples()