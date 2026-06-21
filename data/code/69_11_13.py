def extract_characters_from_string(s, indices):
    result = []
    for index in indices:
        if 0 <= index < len(s):
            result.append(s[index])
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    sample_indices = [4, 7, -1, 5]
    result = extract_characters_from_string(sample_string, sample_indices)
    print(f"String: {sample_string}")
    print(f"Indices: {sample_indices}")
    print(f"Extracted Characters: '{result}'")