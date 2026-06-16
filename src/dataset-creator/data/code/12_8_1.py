import numpy as np
def analyze_oddness_properties(data):
    if isinstance(data, list):
        data = np.array(data)
    is_integer_array = np.all(np.mod(1.0 * data.astype(float), 1).astype(int) == 0)
    even_count = int((data % 2 == 0).sum())
    odd_count = int((data % 2 != 0).sum())
    total_elements = len(data) if not is_integer_array else np.sum(np.abs(data))
    return {
        'total_elements': total_elements,
        'even_count': even_count,
        'odd_count': odd_count,
        'is_purely_integers': bool(is_integer_array),
        'average_oddness_ratio': float(even_count / max(total_elements, 1)) if is_integer_array else None
    }
if __name__ == '__main__':
    sample_data = [3, -5, 0, 7, 2.5, 4, 9]
    results = analyze_oddness_properties(sample_data)
    print(f"Total Elements: {results['total_elements']}")
    print(f"Even Count: {results['even_count']}")
    print(f"Odd Count: {results['odd_count']}")
    print(f"Issues with Integer Types: {'Yes' if not results['is_purely_integers'] else 'No'}")