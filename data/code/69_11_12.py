def fetch_characters_from_string(s, indices):
    result = []
    for index in indices:
        if 0 <= index < len(s):
            result.append(s[index])
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    valid_indices = [0, 7, 12]
    invalid_indices = [-5, 20, 3]

    fetched_characters_valid = fetch_characters_from_string(sample_string, valid_indices)
    print(f"String: {sample_string}")
    print(f"Valid Indices: {valid_indices}")
    print(f"Fetched Characters (Valid): {fetched_characters_valid}")

    fetched_characters_invalid = fetch_characters_from_string(sample_string, invalid_indices)
    print(f"Invalid Indices: {invalid_indices}")
    print(f"Fetched Characters (Invalid): {fetched_characters_invalid}")