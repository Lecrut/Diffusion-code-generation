def check_repeated_characters(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if not char.isalnum():                                                                                       
            continue
        count = char_count.get(char, 0) + 1
        char_count[char] = count
    return len([count for count in char_count.values() if count > 1]) > 0
def main():
    sample_strings = [
        "Hello World",
        "Python Programming",
        "abcdefg"
    ]
    results = []
    for s in sample_strings:
        has_repeat = check_repeated_characters(s)
        result_message = f"'{s}': {'Has repeated characters' if has_repeat else 'No repeated characters'}"
        print(result_message)
        results.append(has_repeat)
if __name__ == '__main__':
    main()