def reverse_words(s):
    if not isinstance(s, str) or not s.strip():
        raise ValueError("Input must be a non-empty string.")
    
    words = s.split()
    reversed_words = words[::-1]
    result = ' '.join(reversed_words)
    return result

if __name__ == '__main__':
    test_string = "hello world this is a test"
    print(reverse_words(test_string))