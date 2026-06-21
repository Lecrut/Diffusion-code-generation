def find_median(values):
    if not values:
        raise ValueError("Input list cannot be empty")
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if n % 2 == 1:
        return sorted_values[n // 2]
    else:
        mid1, mid2 = sorted_values[n // 2 - 1], sorted_values[n // 2]
        return (mid1 + mid2) / 2.0

if __name__ == '__main__':
    sample_input = [10, 5, 20, 15, 30]
    try:
        median_value = find_median(sample_input)
        print(f"The median is: {median_value}")
    except ValueError as e:
        print(e)