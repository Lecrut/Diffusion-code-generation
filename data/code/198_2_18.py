def find_min_value(values):
    try:
        min_val = float('inf')
        for value in values:
            num = float(value)
            if num < min_val:
                min_val = num
        return min_val
    except ValueError:
        raise ValueError("List must contain only numeric strings")

if __name__ == '__main__':
    sample_values1 = ['3.14', '2.718', '1.618', '0.577']
    print(f"Minimum of {sample_values1}: {find_min_value(sample_values1)}")
    
    sample_values2 = ['0.987', '-0.123', '5.432', '-2.1']
    print(f"Minimum of {sample_values2}: {find_min_value(sample_values2)}")