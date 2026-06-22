import string

def count_punctuation(file_path):
    punctuation_freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char in string.punctuation:
                    punctuation_freq[char] = punctuation_freq.get(char, 0) + 1
    return punctuation_freq

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. Testing, one, two, three."
    with open('sample.txt', 'w') as file:
        file.write(sample_text)
    
    result = count_punctuation('sample.txt')
    print(result)