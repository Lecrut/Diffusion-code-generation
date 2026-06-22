INPUT_FILE_PATH = 'sample_input.txt'
OUTPUT_FILE_PATH = 'sorted_output.txt'

def sort_words_in_file(input_path, output_path):
    with open(input_path, 'r') as file:
        words = file.read().splitlines()
    
    sorted_words = sorted(words)
    
    with open(output_path, 'w') as file:
        for word in sorted_words:
            file.write(word + '\n')

if __name__ == '__main__':
    sort_words_in_file(INPUT_FILE_PATH, OUTPUT_FILE_PATH)