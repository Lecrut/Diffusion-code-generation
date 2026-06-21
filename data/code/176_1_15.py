def extract_unique_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text)
    unique_words = []
    seen = set()
    
    for word in words:
        if word.lower() not in seen:
            unique_words.append(word)
            seen.add(word.lower())
    
    return unique_words

if __name__ == '__main__':
    sample_string = "Hello World! This is a test string with numbers 123 and punctuation."
    result = extract_unique_words(sample_string)
    print(result)