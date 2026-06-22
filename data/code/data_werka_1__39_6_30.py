def find_substring_indices(text, pattern):
    indices = []
    index = text.find(pattern)
    while index != -1:
        indices.append((index, index + len(pattern)))
        index = text.find(pattern, index + 1)
    return indices

if __name__ == '__main__':
    sample_text = "hello world, hello universe"
    sample_pattern = "hello"
    result = find_substring_indices(sample_text, sample_pattern)
    print(result)

    another_sample_text = "banana banana apple"
    another_sample_pattern = "banana"
    another_result = find_substring_indices(another_sample_text, another_sample_pattern)
    print(another_result)