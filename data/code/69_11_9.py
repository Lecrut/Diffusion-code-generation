def print_characters_by_indices(input_string, indices):
    for index in indices:
        if 0 <= index < len(input_string):
            print(input_string[index], end='')

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 8, 12]
    print_characters_by_indices(sample_string, sample_indices)