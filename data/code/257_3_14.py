def calculate_complex_difference(complex_data):
    if not complex_data or len(complex_data) < 2:
        raise ValueError("List must contain at least two elements to calculate the difference.")
    
    max_value = max(complex_data, key=lambda x: abs(x))
    min_value = min(complex_data, key=lambda x: abs(x))
    
    return max_value - min_value

if __name__ == '__main__':
    sample1 = [3+4j, 6-8j, 2+3j]
    sample2 = [-1-1j, -2-2j, 0+0j]
    sample3 = [5+12j, 9+12j, 13+5j]
    
    try:
        result1 = calculate_complex_difference(sample1)
        print(f"Difference for {sample1}: {result1}")
    except ValueError as e:
        print(f"Error for {sample1}: {e}")

    try:
        result2 = calculate_complex_difference(sample2)
        print(f"Difference for {sample2}: {result2}")
    except ValueError as e:
        print(f"Error for {sample2}: {e}")

    try:
        result3 = calculate_complex_difference(sample3)
        print(f"Difference for {sample3}: {result3}")
    except ValueError as e:
        print(f"Error for {sample3}: {e}")