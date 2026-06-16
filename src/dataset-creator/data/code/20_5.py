def extract_non_negative(lst):
    return [x for x in lst if isinstance(x, (int, float)) and x >= 0]
if __name__ == '__main__':
    sample_data = [-5, "10", None, 3.7, -2, True, False, [], {"key": 4}]
    result = extract_non_negative(sample_data)
    print(result)