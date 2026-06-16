import numpy as np
def analyze_oddness_properties(data_array):
    try:
        data = np.array([int(x) for x in data_array])
    except (ValueError, TypeError):
        raise ValueError("Input must contain only integers or convertible values.")
    total_elements = len(data)
    is_odd_mask = data % 2 != 0
    odd_count = np.sum(is_odd_mask)
    even_count = total_elements - odd_count
    if total_elements > 0:
        odd_percentage = (odd_count / total_elements) * 100.0
        even_percentage = (even_count / total_elements) * 100.0
        is_odd_dominant = odd_count > even_count
    else:
        odd_percentage = 0.0
        even_percentage = 0.0
        is_odd_dominant = False
    return {
        'total_elements': total_elements,
        'odd_count': int(odd_count),
        'even_count': int(even_count),
        'odd_percentage': odd_percentage,
        'even_percentage': even_percentage,
        'is_odd_dominant': bool(is_odd_dominant)
    }
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5] * 1000
    result = analyze_oddness_properties(sample_data)
    print(f"Total Elements: {result['total_elements']}")
    print(f"Odd Count: {result['odd_count']}")
    print(f"Even Count: {result['even_count']}")
    print(f"Odd Percentage: {result['odd_percentage']:.2f}%")
    print(f"Even Percentage: {result['even_percentage']:.2f}%")
    print(f"Iss Odd Dominant: {result['is_odd_dominant']}")