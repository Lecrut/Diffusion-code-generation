def sort_and_write_words(input_path, output_path):
    with open(input_path, 'r') as file:
        words = [line.strip() for line in file]
    
    words.sort()
    
    with open(output_path, 'w') as file:
        for word in words:
            file.write(word + '\n')

if __name__ == '__main__':
    sample_input_path = 'sample_input.txt'
    sample_output_path = 'sorted_output.txt'
    sort_and_write_words(sample_input_path, sample_output_path)