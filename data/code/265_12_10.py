def remove_duplicates(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    seen = set()
    result = []
    
    for char in phrase:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    sample_phrase1 = "Hello World"
    sample_phrase2 = "Programming is fun"
    sample_phrase3 = "AEIOUaeiou 123"
    
    print(f"'{sample_phrase1}' -> '{remove_duplicates(sample_phrase1)}'")
    print(f"'{sample_phrase2}' -> '{remove_duplicates(sample_phrase2)}'")
    print(f"'{sample_phrase3}' -> '{remove_duplicates(sample_phrase3)}'")