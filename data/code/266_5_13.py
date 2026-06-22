def calculate_average_word_length(file_paths):
    total_words = 0
    total_chars = 0
    
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            total_words += len(words)
            total_chars += sum(len(word) for word in words)
    
    if total_words == 0:
        return 0
    
    average_length = total_chars / total_words
    return average_length

if __name__ == '__main__':
    sample_files = ['sample1.txt', 'sample2.txt', 'sample3.txt']
    average_length = calculate_average_word_length(sample_files)
    print(f"Average word length across files: {average_length:.2f}")