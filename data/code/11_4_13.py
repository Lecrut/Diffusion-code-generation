def find_duplicates(text):
    lower_text = text.lower()
    count_map = {}
    for char in lower_text:
        if char not in count_map:
            count_map[char] = 0
        count_map[char] += 1
    duplicates = set()
    for char, count in count_map.items():
        if count > 1:
            duplicates.add(char)
    return sorted(list(duplicates))

if __name__ == '__main__':
    sample_text = "Hello World"
    result = find_duplicates(sample_text)
    print(result)