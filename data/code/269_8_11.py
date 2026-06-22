import string

def count_punctuation(file_path):
    punctuation_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char in string.punctuation:
                    punctuation_count[char] = punctuation_count.get(char, 0) + 1
    return punctuation_count

if __name__ == '__main__':
    sample_text_file = 'sample.txt'
    result = count_punctuation(sample_text_file)
    print(result)