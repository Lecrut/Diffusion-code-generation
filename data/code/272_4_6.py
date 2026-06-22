def read_words_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        raise ValueError(f"File '{file_path}' not found.")

def write_words_to_file(words, file_path):
    with open(file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')

def sort_and_write_words(input_file_path, output_file_path):
    try:
        words = read_words_from_file(input_file_path)
        sorted_words = sorted(words)
        write_words_to_file(sorted_words, output_file_path)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    input_path = 'sample_input.txt'
    output_path = 'sorted_output.txt'
    sort_and_write_words(input_path, output_path)