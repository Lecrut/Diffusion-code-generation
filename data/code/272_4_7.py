def sort_words(input_file, output_file):
    with open(input_file, 'r') as file:
        words = file.read().splitlines()
    
    sorted_words = sorted(words)
    
    with open(output_file, 'w') as file:
        for word in sorted_words:
            file.write(word + '\n')

if __name__ == '__main__':
    sort_words('input.txt', 'output.txt')