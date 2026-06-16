import numpy as np
def analyze_oddness_properties(data):
    if isinstance(data, list):
        data = np.array(data)
    is_integer_array = np.issubdtype(data.dtype, np.integer)
    total_elements = len(data)
    parities = data % 2
    unique_parity_counts = {0: int(np.sum(parities == 0)), 1: int(np.sum(parities == 1))}
    return {
        'total_elements': total_elements,
        'is_integer_array': is_integer_array,
        'parity_distribution': unique_parity_counts,
        'odd_count': unique_parity_counts[1],
        'even_count': unique_parity_counts[0]
    }
if __name__ == '__main__':
    sample_data = [3, 5, 7, 9, 2, 4, 6, 8, 10, 11, -1, -3, np.float64(1.5), np.int32(-5)]
    result = analyze_oddness_properties(sample_data)
    print(f"Total Elements: {result['total_elements']}")
    print(f"Issues Integer Array: {result['is_integer_array']}")
    print(f"Parity Distribution (Even/Odd): {result['parity_distribution']}")
    print(f"Odd Count: {result['odd_count']}")
    print(f"Even Count: {result['even_count']}")