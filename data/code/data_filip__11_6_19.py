def find_repeated_characters(s):
    seen = set()
    repeated = set()
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
    
    seen_again = set()
    result = []
    for char in s:
        if char in repeated and char not in seen_again:
            result.append(char)
            seen_again.add(char)
    
    return result

if __name__ == '__main__':
    sample_string = "programming"
    repeated_chars = find_repeated_characters(sample_string)
    print(repeated_chars)