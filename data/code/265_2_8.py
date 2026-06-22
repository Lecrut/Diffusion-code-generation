def extract_non_repeated_chars(phrase):
    char_count = {}
    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    non_repeated_chars = [char for char, count in char_count.items() if count == 1]
    
    result = ""
    for char in phrase:
        if char in non_repeated_chars:
            result += char
            
    return result

if __name__ == '__main__':
    sample_phrase = "Hello World! 123"
    result = extract_non_repeated_chars(sample_phrase)
    print(result)