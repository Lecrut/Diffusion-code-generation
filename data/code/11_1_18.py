def find_duplicate_chars(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    duplicates = [char for char, count in counts.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "programming"
    result = find_duplicate_chars(sample_text)
    print(result)