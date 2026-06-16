import numpy as np
def analyze_oddness_properties(data):
    if isinstance(data, list):
        data = np.array(data)
    is_integer_array = np.all(np.mod(1.0 * data.astype(float), 1).astype(int) == 0)
    even_count = int((data % 2 == 0).sum())
    odd_count = int((data % 2 != 0).sum())
    total_elements = len(data)
    if is_integer_array and total_elements > 0:
        ratio_odd_even = float(odd_count / even_count) if even_count > 0 else float('inf')
        return {
            'is_purely_integers': True,
            'total_elements': int(total_elements),
            'even_count': int(even_count),
            'odd_count': int(odd_count),
            'ratio_odd_even': ratio_odd_even if not np.isinf(ratio_odd_even) else float('nan')
        }
    return {
        'is_purely_integers': False,
        'total_elements': int(total_elements),
        'even_count': int(even_count),
        'odd_count': int(odd_count),
        'ratio_odd_even': None
    }
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8] + list(range(90, 100))
    result = analyze_oddness_properties(sample_data)
    print(f"Total Elements: {result['total_elements']}")
    print(f"Even Count: {result['even_count']}")
    print(f"Odd Count: {result['odd_count']}")
    if 'ratio_odd_even' in result and result['ratio_odd_even'] is not None:
        print(f"Ratio (Odd/Even): {result['ratio_odd_even']}")