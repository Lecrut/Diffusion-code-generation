def find_repeated_chars(s):
    seen = set()
    repeated = set()
    
    for char in s:
        if char in seen:
            repeated.add(char)
        else:
            seen.add(char)
            
    return sorted(repeated)

if __name__ == '__main__':
    text = "programming"
    result = find_repeated_chars(text)
    print(result)