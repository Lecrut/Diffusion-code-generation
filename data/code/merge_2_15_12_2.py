import timeit
def sort_numeric_data(data):
    if isinstance(data, list):
        return sorted(data)
    elif hasattr(data, '__iter__') and not isinstance(data, str):
        result = []
        for item in data:
            try:
                float(item)
                result.append(float(item))
            except (ValueError, TypeError):
                continue
        return sorted(result)
    else:
        raise ValueError("Input must be iterable of numerical values.")
if __name__ == '__main__':
    sample_data = [3.14, 2.718, -0.5, "9", True, None]
    cleaned_sample = []
    for item in sample_data:
        if isinstance(item, (int, float)):
            cleaned_sample.append(float(item))
        elif str(item).replace('.', '').isdigit():
            cleaned_sample.append(float(str(item)))
    start_time = timeit.default_timer()
    sorted_result = sort_numeric_data(cleaned_sample)
    end_time = timeit.default_timer()
    print(f"Sorted data: {sorted_result}")
    print(f"Time taken (seconds): {end_time - start_time:.6f}")