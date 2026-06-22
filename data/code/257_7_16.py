def calculate_difference_of_extremes(d: dict) -> int:
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary.")
    if len(d) == 0:
        raise ValueError("Dictionary cannot be empty.")
    
    values = list(d.values())
    return max(values) - min(values)

if __name__ == '__main__':
    sample_dict_1 = {'a': 1, 'b': 5, 'c': 2}
    result_1 = calculate_difference_of_extremes(sample_dict_1)
    print(f"Dictionary: {sample_dict_1}")
    print(f"Difference of extremes: {result_1}")

    sample_dict_2 = {'x': -10, 'y': 0, 'z': 5}
    result_2 = calculate_difference_of_extremes(sample_dict_2)
    print(f"\nDictionary: {sample_dict_2}")
    print(f"Difference of extremes: {result_2}")

    sample_dict_3 = {'m': 42}
    result_3 = calculate_difference_of_extremes(sample_dict_3)
    print(f"\nDictionary: {sample_dict_3}")
    print(f"Difference of extremes: {result_3}")