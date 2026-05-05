def print_indexed_characters(text, indices):
    for index in indices:
        if 0 <= index < len(text):
            print(text[index], end=' ')
        else:
            print(f"Index {index} out of bounds.")
if __name__ == '__main__':
    sample_string = "HelloWorld"
    sample_indices = [0, 4, 7, 10, -1]
    print_indexed_characters(sample_string, sample_indices)