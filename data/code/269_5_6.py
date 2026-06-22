import string

def find_unique_punctuation(text):
    punctuation = set(string.punctuation)
    unique_punctuation = [char for char in text if char in punctuation]
    return list(set(unique_punctuation))

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test. It contains: punctuation marks like @#$%^&*()_+{}|:\"<>?[];',./`~"
    result = find_unique_punctuation(sample_text)
    print(result)