import string

def isolate_and_sort_punctuation(input_string):
    punctuation_set = set(string.punctuation)
    isolated_punctuations = sorted([char for char in input_string if char in punctuation_set])
    return ''.join(isolated_punctuations)
if __name__ == '__main__':
    sample_string = 'Hello, World! This is a test. 123.'
    result = isolate_and_sort_punctuation(sample_string)
    print(result)