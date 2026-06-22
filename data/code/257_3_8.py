def calculate_difference(complex_numbers):
    if not complex_numbers:
        raise ValueError("List must contain at least one element to calculate the difference.")
    return max(complex_numbers) - min(complex_numbers)

if __name__ == '__main__':
    sample_values = [
        [1+2j, 3+4j, 5+6j],
        [-1-1j, -2-2j, -3-3j],
        [0+0j, 0+0j],
        [10+20j]
    ]
    
    for values in sample_values:
        try:
            result = calculate_difference(values)
            print(f"Difference for {values}: {result}")
        except ValueError as e:
            print(f"Error for {values}: {e}")