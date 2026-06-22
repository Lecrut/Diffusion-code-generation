def find_duplicate_characters(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
    duplicates = []
    for char, count in counts.items():
        if count > 1:
            duplicates.append(char)
    return duplicates

if __name__ == '__main__':
    sample_string = "Programming"
    result = find_duplicate_characters(sample_string)
    print(result)