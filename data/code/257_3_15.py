def calculate_complex_difference(numbers):
    if not numbers:
        raise ValueError("List must contain at least one element.")
    min_value = min(numbers, key=lambda x: (x.real, x.imag))
    max_value = max(numbers, key=lambda x: (x.real, x.imag))
    return max_value - min_value

if __name__ == '__main__':
    sample1 = [3+4j, 1+2j, 5-1j]
    sample2 = [10+10j, -5+5j, 0+0j]
    
    try:
        result1 = calculate_complex_difference(sample1)
        print(f"Difference for {sample1}: {result1}")
        
        result2 = calculate_complex_difference(sample2)
        print(f"Difference for {sample2}: {result2}")
        
    except ValueError as e:
        print(e)