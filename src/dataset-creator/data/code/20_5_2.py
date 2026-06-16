def extract_non_negative(lst):
    return [item for item in lst if isinstance(item, (int, float)) and item >= 0]
if __name__ == '__main__':
    sample_data = [-5, "a", None, 10.5, -3, True, 20, [], {}]
    result = extract_non_negative(sample_data)
    print(result)