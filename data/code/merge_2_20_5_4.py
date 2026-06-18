def extract_non_negative(data):
    return [item for item in data if isinstance(item, (int, float)) and item >= 0]
if __name__ == '__main__':
    sample_data = [-5, "negative", None, 3.14, -2, True, 0, False, "invalid"]
    result = extract_non_negative(sample_data)
    print(result)