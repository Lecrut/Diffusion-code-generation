def extract_non_negative(numbers):
    result = []
    for item in numbers:
        try:
            if isinstance(item, (int, float)) and item >= 0:
                result.append(float(item) if not isinstance(item, int) else item)
        except Exception:
            continue
    return result
if __name__ == '__main__':
    sample_data = [1, -2.5, "abc", None, True, 3.7, object(), 0]
    output = extract_non_negative(sample_data)
    print(output)