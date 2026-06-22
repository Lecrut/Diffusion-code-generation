def compare_two_simple_quantities_now_summary(quantity1, quantity2):
    mean = (quantity1 + quantity2) / 2
    variance = ((quantity1 - mean) ** 2 + (quantity2 - mean) ** 2) / 2
    difference = abs(quantity1 - quantity2)
    return {
        'mean': mean,
        'variance': variance,
        'difference': difference
    }

if __name__ == '__main__':
    sample_values = [
        (3.1415926535, 3.1415926536),
        (0.1 + 0.2, 0.3),
        (1.0, 0.9999999999999999)
    ]
    for values in sample_values:
        result = compare_two_simple_quantities_now_summary(*values)
        print(f"Summary statistics for {values}: {result}")