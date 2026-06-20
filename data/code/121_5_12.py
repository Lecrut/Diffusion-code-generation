def compare_complex_numbers(c1, c2):
    if not isinstance(c1, complex) or not isinstance(c2, complex):
        raise ValueError("Both inputs must be complex numbers.")
    
    abs_c1 = abs(c1)
    abs_c2 = abs(c2)
    
    return abs_c1, abs_c2

if __name__ == '__main__':
    c1 = 3 + 4j
    c2 = -1 - 1j
    
    abs_c1, abs_c2 = compare_complex_numbers(c1, c2)
    
    print(f"Absolute value of c1: {abs_c1}")
    print(f"Absolute value of c2: {abs_c2}")