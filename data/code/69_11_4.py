def print_chars_at_positions(s, indices):
    for index in indices:
        if 0 <= index < len(s):
            print(s[index])

if __name__ == '__main__':
    sample_string = "hello world"
    sample_indices = [1, 3, 5, 7, 9]
    print_chars_at_positions(sample_string, sample_indices)