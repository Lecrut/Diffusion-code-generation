def find_repeated_letters(input_string):
    seen = set()
    repeated = set()
    for char in input_string:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in seen:
                repeated.add(lower_char)
            else:
                seen.add(lower_char)
    return sorted(repeated)

if __name__ == '__main__':
    test_cases = [
        "programming",
        "hello world",
        "abcdefg",
        "aabbccddeeff",
        "Python is great!"
    ]
    
    for test in test_cases:
        print(f"Input: '{test}'")
        result = find_repeated_letters(test)
        print("Repeated letters found:", result)