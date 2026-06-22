import string

def count_punctuation(text):
    punctuation_dict = {}
    for char in text:
        if char in string.punctuation:
            if char in punctuation_dict:
                punctuation_dict[char] += 1
            else:
                punctuation_dict[char] = 1
    return punctuation_dict

if __name__ == '__main__':
    sample_text = "Hello, world! How are you? This is a test string with symbols @#$ and numbers 123."
    result = count_punctuation(sample_text)
    print(result)