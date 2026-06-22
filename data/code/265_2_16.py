def extract_non_repeating_chars(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    non_repeating_chars = [char for char, count in char_count.items() if count == 1]
    
    result = ""
    for char in text:
        if char in non_repeating_chars:
            result += char
            
    return result

if __name__ == '__main__':
    sample_text = "Hello World! 123"
    result = extract_non_repeating_chars(sample_text)
    print(result)