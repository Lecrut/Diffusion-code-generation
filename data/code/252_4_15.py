def compare_two_simple_quantities_now_summary(a, b):
    mean = (a + b) / 2
    difference = abs(a - b)
    min_value = min(a, b)
    max_value = max(a, b)
    return {
        'mean': mean,
        'difference': difference,
        'min': min_value,
        'max': max_value
    }

if __name__ == '__main__':
    sample_a = 15.2
    sample_b = 8.7
    result = compare_two_simple_quantities_now_summary(sample_a, sample_b)
    print(f"Summary for {sample_a} and {sample_b}: {result}")