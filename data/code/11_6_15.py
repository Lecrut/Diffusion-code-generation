def find_repeated_chars(text):
    if not text:
        return set()
    
    seen = set()
    repeated = set()
    
    for char in text:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
            
    return repeated

if __name__ == '__main__':
    sample_input = "programming"
    result = find_repeated_chars(sample_input)
    print(result)