def print_chars_by_indices(s: str, indices: list):
    for index in indices:
        if 0 <= index < len(s):
            print(s[index], end='')

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [1, 3, 5, 7, 9]
    print_chars_by_indices(sample_string, sample_indices)