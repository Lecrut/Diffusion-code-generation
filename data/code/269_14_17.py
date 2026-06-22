import string

def isolate_and_sort_punctuation(input_string):
    punctuation_set = set(string.punctuation)
    isolated_punctuation = [char for char in input_string if char in punctuation_set]
    sorted_punctuation = ''.join(sorted(isolated_punctuation, key=str.lower))
    return sorted_punctuation
if __name__ == '__main__':
    sample_input = 'Hello, World! This is a test. 123.'
    result = isolate_and_sort_punctuation(sample_input)
    print(result)