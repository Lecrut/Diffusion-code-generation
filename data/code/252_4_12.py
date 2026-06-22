def compare_two_simple_quantities_now_summary():
    values = [3.1415926535, 0.1 + 0.2, 1.0]
    min_value = min(values)
    max_value = max(values)
    mean_value = sum(values) / len(values)
    return {
        'min': min_value,
        'max': max_value,
        'mean': mean_value
    }

if __name__ == '__main__':
    result = compare_two_simple_quantities_now_summary()
    print(f"Minimum value: {result['min']}")
    print(f"Maximum value: {result['max']}")
    print(f"Mean value: {result['mean']}")