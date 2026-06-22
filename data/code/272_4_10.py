def sort_words_from_file(input_file_path):
    with open(input_file_path, 'r') as file:
        words = file.read().split()
    
    words.sort()
    
    return words

if __name__ == '__main__':
    sorted_words = sort_words_from_file('sample_input.txt')
    print(sorted_words)