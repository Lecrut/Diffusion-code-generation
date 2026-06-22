def count_word_lengths(file_path):
    word_lengths = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                length = len(word)
                if length in word_lengths:
                    word_lengths[length] += 1
                else:
                    word_lengths[length] = 1
    return word_lengths

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    result = count_word_lengths(sample_file_path)
    print(result)