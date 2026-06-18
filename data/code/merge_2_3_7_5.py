import numpy as np
def check_evenness_fast(values: list) -> dict:
    if not isinstance(values, list) or len(values) == 0:
        return {
            'total': 0,
            'even_count': 0,
            'odd_count': 0,
            'min_val': None,
            'max_val': None,
            'mean_val': None,
            'is_all_even': True if len(values) == 0 else False
        }
    even_count = sum(1 for v in values if (v & 1) == 0)
    odd_count = len(values) - even_count
    stats_array = np.array(values)
    return {
        'total': len(values),
        'even_count': int(even_count),
        'odd_count': int(odd_count),
        'min_val': float(stats_array.min()),
        'max_val': float(stats_array.max()),
        'mean_val': float(np.mean(stats_array)),
        'is_all_even': odd_count == 0,
        '_bitwise_check_used': True
    }
if __name__ == '__main__':
    sample_data = [24, -18, 57, 36, 9, 100]
    result = check_evenness_fast(sample_data)
    print(f"Total values: {result['total']}")
    print(f"Even count: {result['even_count']}")
    print(f"Odd count: {result['odd_count']}")
    print(f"All even? {result['is_all_even']}")