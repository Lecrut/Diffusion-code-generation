def extract_non_negative(lst):
    result = []
    for item in lst:
        try:
            if isinstance(item, (int, float)) and item >= 0:
                result.append(float(item) if not isinstance(item, int) else item)
        except Exception:
            continue
    return result
if __name__ == '__main__':
    sample_data = [1, -5, "a", None, 3.5, True, False, object(), 0]
    output = extract_non_negative(sample_data)
    print(output)