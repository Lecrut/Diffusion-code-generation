def count_repeated_characters(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    repeated_chars = {char: count for char, count in char_counts.items() if count > 1}
    return repeated_chars

if __name__ == '__main__':
    sample_string = "hello world"
    result = count_repeated_characters(sample_string)
    print(result)