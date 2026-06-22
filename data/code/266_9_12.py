def word_length_frequency(file_path):
    frequency = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                for word in words:
                    length = len(word)
                    if length not in frequency:
                        frequency[length] = 0
                    frequency[length] += 1
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return frequency

if __name__ == '__main__':
    sample_file = "sample.txt"
    result = word_length_frequency(sample_file)
    print(result)