def find_duplicate_characters(text):
    char_count = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "Programming in Python is fun"
    result = find_duplicate_characters(sample_string)
    print(result)