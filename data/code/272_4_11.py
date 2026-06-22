def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

def write_sorted_words_to_file(words, output_file_path):
    sorted_words = sorted(words)
    with open(output_file_path, 'w') as file:
        for word in sorted_words:
            file.write(word + '\n')

if __name__ == '__main__':
    try:
        input_file_path = 'sample_input.txt'
        output_file_path = 'sorted_output.txt'

        words = read_words_from_file(input_file_path)
        write_sorted_words_to_file(words, output_file_path)

        print(f"Words have been sorted and written to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")