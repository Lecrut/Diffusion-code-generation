def get_lower_median(values):
    if not values:
        raise ValueError("Cannot compute median of an empty list")
    sorted_values = sorted(values)
    length = len(sorted_values)
    if length % 2 == 1:
        return sorted_values[length // 2]
    return sorted_values[(length // 2) - 1]

def process_medians(input_data):
    results = {}
    for key, val in input_data.items():
        results[key] = get_lower_median(val)
    return results

if __name__ == '__main__':
    test_cases = {
        "odd_list": [3, 1, 4, 1, 5],
        "even_list": [10, 20, 30, 40],
        "single": [42],
        "negative": [-5, -1, -10, -2]
    }
    output = process_medians(test_cases)
    for k, v in output.items():
        print(v)