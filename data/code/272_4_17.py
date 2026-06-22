def sort_words_in_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        words = file.read().splitlines()
    
    sorted_words = sorted(words)
    
    with open(output_file_path, 'w') as file:
        for word in sorted_words:
            file.write(word + '\n')

if __name__ == '__main__':
    input_file_path = 'sample_input.txt'
    output_file_path = 'sorted_output.txt'
    sort_words_in_file(input_file_path, output_file_path)