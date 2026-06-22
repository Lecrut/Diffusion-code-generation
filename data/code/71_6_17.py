def get_lower_median(values):
    if not isinstance(values, (list, tuple)):
        raise ValueError("Input must be a list or tuple")
    if len(values) == 0:
        raise ValueError("Input list cannot be empty")
    sorted_vals = sorted(values)
    count = len(sorted_vals)
    if count % 2 == 1:
        return sorted_vals[count // 2]
    return sorted_vals[count // 2 - 1]

if __name__ == '__main__':
    sample_odd = [34, 15, 88, 2, 91]
    sample_even = [12, 45, 3, 67]
    sample_single = [100]
    
    print(get_lower_median(sample_odd))
    print(get_lower_median(sample_even))
    print(get_lower_median(sample_single))