def find_repeated_chars(text):
    seen = {}
    for char in text:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    return ''.join(char for char, count in seen.items() if count > 1)

if __name__ == '__main__':
    result = find_repeated_chars("programming")
    print(result)