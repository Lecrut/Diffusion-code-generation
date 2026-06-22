def count_words(file_path):
    word_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            word_count += len(words)
    return word_count

if __name__ == '__main__':
    sample_text = "Python is an interpreted, high-level and general-purpose programming language.\nIt was created by Guido van Rossum and first released in 1991."
    temp_file_path = 'sample.txt'
    with open(temp_file_path, 'w') as file:
        file.write(sample_text)
    result = count_words(temp_file_path)
    print(result)