def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def sort_words(words):
    words.sort()
    return words

def write_sorted_words_to_file(sorted_words, output_file_path):
    with open(output_file_path, 'w') as file:
        for word in sorted_words:
            file.write(word + '\n')

if __name__ == '__main__':
    input_file_path = 'sample_input.txt'
    output_file_path = 'sorted_output.txt'

    words = read_words_from_file(input_file_path)
    sorted_words = sort_words(words)
    write_sorted_words_to_file(sorted_words, output_file_path)