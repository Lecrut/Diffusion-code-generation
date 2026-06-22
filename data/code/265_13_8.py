def most_frequent_chars(phrase):
    if not isinstance(phrase, str):
        raise ValueError("Input must be a string")
    
    char_count = {}
    for char in phrase:
        char_count[char] = char_count.get(char, 0) + 1
    
    max_count = max(char_count.values())
    return [char for char, count in char_count.items() if count == max_count]

if __name__ == '__main__':
    sample_phrase = "hello world"
    result = most_frequent_chars(sample_phrase)
    print(result)