def count_consonants(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    vowels = set('aeiouAEIOU')
    
    consonant_set = valid_chars - vowels
    
    count = 0
    for character in text:
        if character in consonant_set:
            count += 1
            
    return count

if __name__ == '__main__':
    sample_text = "Python is powerful!"
    result = count_consonants(sample_text)
    print(result)