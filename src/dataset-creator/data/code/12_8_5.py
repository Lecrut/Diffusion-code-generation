import numpy as np
def is_odd_pure_python(value):
    return value % 2 != 0
def analyze_dataset(data_array):
    odd_count = sum(1 for x in data_array if isinstance(x, (int, float)) and is_odd_pure_python(int(round(x))))
    even_count = len(data_array) - odd_count
    total_sum = np.sum(np.array([x if isinstance(x, int) else round(float(x), 6) for x in data_array]))
    return {
        'total_elements': len(data_array),
        'odd_values': [int(round(x)) for x in data_array if is_odd_pure_python(int(round(x)))],
        'even_values': [x for x in data_array if not (isinstance(x, int) or isinstance(x, float))] +\
                     [int(round(x)) for x in data_array if not is_odd_pure_python(int(round(x))) and isinstance(x, (int, float))],
        'odd_count': odd_count,
        'even_count': even_count,
        'total_sum': total_sum,
        'mean_value': total_sum / len(data_array) if len(data_array) > 0 else 0.0
    }
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, np.int64(7), float('8'), -9]
    result = analyze_dataset(sample_data)
    print(f"Total Elements: {result['total_elements']}")
    print(f"Odd Count: {result['odd_count']}")
    print(f"Even Count: {result['even_count']}")
    print(f"Sum of Values: {result['total_sum']}")
    print(f"Mean Value: {result['mean_value']:.2f}")