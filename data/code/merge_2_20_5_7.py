def extract_non_negative(lst):
    return [item for item in lst if isinstance(item, (int, float)) and item >= 0]
if __name__ == '__main__':
    sample_data = [-5, "10", None, 3.7, -2.1, True, False, object(), 42]
    result = extract_non_negative(sample_data)
    print(result)