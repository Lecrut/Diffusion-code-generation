def print_chars_by_indices(s, indices):
    for index in indices:
        if 0 <= index < len(s):
            print(s[index], end='')
    print()

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 12]
    print_chars_by_indices(sample_string, sample_indices)