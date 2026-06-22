def calculate_difference(data):
    if len(data) < 2:
        raise ValueError("List must contain at least two elements to calculate the difference.")
    min_value = min(data)
    max_value = max(data)
    return max_value - min_value

if __name__ == '__main__':
    sample1 = [3+4j, 1+7j, 5-2j, 8+1j]
    sample2 = [-1-1j, -2-3j, -4-4j, -5-5j]
    
    try:
        result1 = calculate_difference(sample1)
        print(f"Difference for {sample1}: {result1}")
    except ValueError as e:
        print(f"Error for {sample1}: {e}")
    
    try:
        result2 = calculate_difference(sample2)
        print(f"Difference for {sample2}: {result2}")
    except ValueError as e:
        print(f"Error for {sample2}: {e}")