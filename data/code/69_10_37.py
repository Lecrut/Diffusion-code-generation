def extract_characters_by_indices(s, indices):
    STRING_LENGTH_THRESHOLD = len(s)
    INVALID_INDEX_VALUE = None

    def is_valid_index(index):
        return isinstance(index, int) and 0 <= index < STRING_LENGTH_THRESHOLD

    valid_indices = [i for i in indices if is_valid_index(i)]
    result = ''.join(s[i] for i in valid_indices)
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 8, 12, 5, 10]
    print(extract_characters_by_indices(sample_string, sample_indices))