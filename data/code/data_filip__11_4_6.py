def find_duplicate_characters(text):
    if not text:
        return []
    frequency = {}
    for char in text.lower():
        if char.isalpha() or char.isdigit() or char == ' ':
            frequency[char] = frequency.get(char, 0) + 1
    duplicates = [char for char, count in frequency.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "Programming is Fun"
    result = find_duplicate_characters(sample_string)
    print(result)