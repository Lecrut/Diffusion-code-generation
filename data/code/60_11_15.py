def compute_factorial(target_value):
    if not isinstance(target_value, int) or target_value < 0:
        raise ValueError("Input must be a non-negative integer")
    
    accumulator = 1
    current_step = 2
    while current_step <= target_value:
        accumulator *= current_step
        current_step += 1
    return accumulator

if __name__ == '__main__':
    sample_n = 20
    result = compute_factorial(sample_n)
    print(result)