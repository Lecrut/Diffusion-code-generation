def average_word_length(file_paths):
    total_words = 0
    total_characters = 0

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            total_words += len(words)
            total_characters += sum(len(word) for word in words)

    if total_words == 0:
        return 0

    average_length = total_characters / total_words
    return average_length

if __name__ == '__main__':
    sample_files = ['file1.txt', 'file2.txt']
    print(average_word_length(sample_files))