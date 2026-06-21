def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])

if __name__ == '__main__':
    test_string = "hello world this is a test"
    if not isinstance(test_string, str) or not test_string.strip():
        raise ValueError("Input must be a non-empty string")
    
    result = reverse_words(test_string)
    print(result)