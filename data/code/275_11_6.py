def sum_even_values(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary")
    
    total = 0
    for value in input_dict.values():
        if isinstance(value, int) and value % 2 == 0:
            total += value
        elif isinstance(value, float):
            continue
        else:
            raise ValueError(f"Non-integer or non-float value found: {value}")
    
    return total

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 'a', 6: 7.8, 8: 10}
    result = sum_even_values(sample_dict)
    print(result)