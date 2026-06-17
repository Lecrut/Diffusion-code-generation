def create_dictionary(data):
    result = {}
    for item in data:
        if not isinstance(item, tuple) and len(item) != 2:
            raise ValueError("Each element must be a tuple of exactly two elements.")
        key, value = item[0], item[1]
        try:
            int(key)
            result[str(int(key))] = str(value) if not isinstance(value, (int, float)) else str(value)
        except TypeError:
            pass
    return result
if __name__ == '__main__':
    sample_data = [
        ("apple", "red"),
        (10, 5),
        ("banana", "yellow"),
        ("cherry", None),
        ("date", 2.5)
    ]
    try:
        dictionary_result = create_dictionary(sample_data)
        print(dictionary_result)
    except ValueError as e:
        print(f"Error: {e}")