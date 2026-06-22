def extract_unique_chars(phrase):
    unique_chars = []
    char_set = set()
    
    for char in phrase:
        if char not in char_set:
            unique_chars.append(char)
            char_set.add(char)
    
    return unique_chars

if __name__ == '__main__':
    sample_phrase1 = "hello world"
    sample_phrase2 = "programming is fun"
    sample_phrase3 = "AEIOUaeiou123"
    
    print(extract_unique_chars(sample_phrase1))
    print(extract_unique_chars(sample_phrase2))
    print(extract_unique_chars(sample_phrase3))