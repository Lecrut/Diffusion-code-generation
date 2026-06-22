def count_words(text):
    word_list = text.split()
    return len(word_list)

def calculate_average_word_length(file_paths):
    total_words = 0
    num_files = len(file_paths)
    
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            words = count_words(content)
            total_words += words
    
    average_length = total_words / num_files if num_files > 0 else 0
    return average_length

if __name__ == '__main__':
    sample_files = ['sample1.txt', 'sample2.txt', 'sample3.txt']
    average_length = calculate_average_word_length(sample_files)
    print(f"The average word length across all files is: {average_length:.2f}")