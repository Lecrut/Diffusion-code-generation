def reverse_words(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    sample_string = "The quick brown fox"
    if not isinstance(sample_string, str):
        raise ValueError("Input must be a string")
    
    reversed_string = reverse_words(sample_string)
    print(reversed_string)