def count_word_lengths(file_path):
    word_length_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                length = len(word)
                if length in word_length_count:
                    word_length_count[length] += 1
                else:
                    word_length_count[length] = 1
    return word_length_count

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    print(count_word_lengths(sample_file_path))