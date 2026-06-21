def print_characters_by_indices(s, indices):
    for index in indices:
        if 0 <= index < len(s):
            print(s[index], end='')
        else:
            print('Index out of range', end='')

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [4, 7, 10, 15]
    print_characters_by_indices(sample_string, sample_indices)