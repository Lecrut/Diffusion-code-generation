def average_word_length(file_paths):
    total_words = 0
    total_chars = 0

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                total_words += len(words)
                total_chars += sum(len(word) for word in words)

    if total_words == 0:
        return 0

    return total_chars / total_words

if __name__ == '__main__':
    sample_files = ['sample1.txt', 'sample2.txt']
    print(average_word_length(sample_files))