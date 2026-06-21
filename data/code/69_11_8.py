def print_characters_by_indices(input_string, indices):
    for index in indices:
        if 0 <= index < len(input_string):
            print(input_string[index])
        else:
            print("Index out of range")

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 12, 5, 15]
    print_characters_by_indices(sample_string, sample_indices)