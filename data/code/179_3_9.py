def reverse_words(s):
    if not isinstance(s, str) or not s:
        raise ValueError("Input must be a non-empty string")
    
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    test_string = "The quick brown fox"
    try:
        result = reverse_words(test_string)
        print(result)
    except ValueError as e:
        print(e)