def extract_non_repeated_chars(phrase):
    char_count = {}
    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    non_repeated_chars = [char for char, count in char_count.items() if count == 1]
    
    result = []
    for char in phrase:
        if char in non_repeated_chars and char not in result:
            result.append(char)
    
    return ''.join(result)

if __name__ == '__main__':
    sample_phrase = "programming is fun"
    print(extract_non_repeated_chars(sample_phrase))