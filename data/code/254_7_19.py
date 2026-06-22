def find_smallest_magnitude_complex(complex_list):
    if not complex_list:
        raise ValueError("The list is empty.")
    
    smallest = min(complex_list, key=lambda x: abs(x))
    return smallest

if __name__ == '__main__':
    sample_values = [3+4j, 1-1j, -2+2j, 0+5j]
    try:
        result = find_smallest_magnitude_complex(sample_values)
        print(result)
    except ValueError as e:
        print(e)