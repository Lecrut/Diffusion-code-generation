import string

def find_unique_punctuation(text):
    punctuation = set()
    for char in text:
        if char in string.punctuation:
            punctuation.add(char)
    return list(punctuation)

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string (with some symbols...)"
    result = find_unique_punctuation(sample_string)
    print(result)