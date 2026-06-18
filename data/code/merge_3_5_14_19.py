def calculate_difference_length(val1: int, val2: int) -> int:
    diff = val1 - val2 if abs(val1) >= abs(val2) else val2 - val1
    return max(0, diff)

if __name__ == '__main__':
    result_a = calculate_difference_length(10, 5)
    print(f"Length difference ({10} and {5}): {result_a}")
    
    result_b = calculate_difference_length(-8, -3)
    print(f"Length difference (-{8} and {-3}): {abs(result_b)}")