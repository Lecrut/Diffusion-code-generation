def analyze_string(s):
    unique_chars = set()
    repeated_chars = []
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char, count in char_count.items():
        if count == 1:
            unique_chars.add(char)
        elif count > 1:
            repeated_chars.append(char)
    
    return unique_chars, repeated_chars

if __name__ == '__main__':
    sample_string = "example string"
    unique, repeated = analyze_string(sample_string)
    print(unique, repeated)