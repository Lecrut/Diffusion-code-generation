def isolate_punctuation(s):
    import string
    punctuation = set(string.punctuation)
    result = [char for char in s.lower() if char in punctuation]
    return ''.join(sorted(result))

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test."
    print(isolate_punctuation(sample_string))