def get_opposite_truth_value(value):
    if value.lower() == 'true':
        return 'False'
    elif value.lower() == 'false':
        return 'True'
    else:
        raise ValueError("Input must be a valid boolean string")

if __name__ == '__main__':
    sample1 = 'True'
    opposite1 = get_opposite_truth_value(sample1)
    print(f"Original: {sample1}, Opposite: {opposite1}")
    
    sample2 = 'false'
    opposite2 = get_opposite_truth_value(sample2)
    print(f"Original: {sample2}, Opposite: {opposite2}")