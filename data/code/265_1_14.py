def extract_unique_characters(phrase):
    unique_chars = []
    seen_chars = set()
    
    for char in phrase:
        if char not in seen_chars:
            unique_chars.append(char)
            seen_chars.add(char)
    
    return unique_chars

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(extract_unique_characters(sample_phrase))