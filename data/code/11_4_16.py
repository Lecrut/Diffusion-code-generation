def find_duplicates(text: str) -> list:
    counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha() or char.isdigit() or char == ' ':
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    
    result = []
    for char, count in counts.items():
        if count > 1:
            result.append(char)
    
    return result

if __name__ == '__main__':
    sample_string = "Hello, World! Hello."
    duplicates = find_duplicates(sample_string)
    print(duplicates)