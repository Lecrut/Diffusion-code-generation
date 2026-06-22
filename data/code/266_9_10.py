def word_length_frequency(file_path):
    frequency = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                length = len(word)
                if length in frequency:
                    frequency[length] += 1
                else:
                    frequency[length] = 1
    return frequency

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    result = word_length_frequency('sample.txt')
    print(result)