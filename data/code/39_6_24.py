def find_substring_indices(text, substring):
    indices = []
    start = 0
    while True:
        start = text.find(substring, start)
        if start == -1:
            break
        end = start + len(substring) - 1
        indices.append((start, end))
        start += 1
    return indices

if __name__ == '__main__':
    text = "This is a test string. This test is just a test."
    substring = "test"
    result = find_substring_indices(text, substring)
    print(result)