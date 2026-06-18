import numpy as np
def analyze_oddness_properties(data_array):
    int_data = data_array.astype(np.int64)
    is_odd_vectorized = int_data % 2 != 0
    total_count = len(int_data)
    odd_count = np.sum(is_odd_vectorized)
    if total_count > 0:
        odd_percentage = (odd_count / total_count) * 100.0
    else:
        odd_percentage = 0.0
    max_odd_value = int_data[is_odd_vectorized].max() if np.any(is_odd_vectorized) else None
    min_odd_value = int_data[is_odd_vectorized].min() if np.any(is_odd_vectorized) else None
    return {
        'total_elements': total_count,
        'odd_elements': odd_count,
        'even_elements': total_count - odd_count,
        'odd_percentage': round(odd_percentage, 2),
        'max_odd_value': max_odd_value,
        'min_odd_value': min_odd_value
    }
def main():
    sample_data = np.concatenate([np.arange(10**6), [2, 3, 5, -7, 42]])
    print("Analyzing Oddness Properties in Large Dataset")
    print("=" * 50)
    results = analyze_oddness_properties(sample_data)
    output_str = (f"Total Elements: {results['total_elements']}\n"
                  f"Odd Elements: {results['odd_elements']}\n"
                  f"Even Elements: {results['even_elements']}\n"
                  f"Odd Percentage: {results['odd_percentage']}%\n")
    if results['max_odd_value'] is not None and results['min_odd_value'] is not None:
        output_str += (f"Max Odd Value: {results['max_odd_value']}\n"
                       f"Min Odd Value: {results['min_odd_value']}\n")
    print(output_str)
if __name__ == '__main__':
    main()