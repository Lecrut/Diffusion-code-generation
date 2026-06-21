def reverse_words(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

if __name__ == '__main__':
    sample_string = "hello world this is a test"
    result = reverse_words(sample_string)
    print(result)