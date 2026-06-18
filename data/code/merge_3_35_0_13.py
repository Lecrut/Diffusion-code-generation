def count_vowels(text):
    """Counts the total number of vowels (a, e, i, o, u) in a string case-insensitively."""
    text = text.lower()
    return sum(1 for char in text if char in 'aeiou')

if __name__ == '__main__':
    test_strings = [
        "Hello, World!",
        "AEIOU",
        "rhythm",
        ""
    ]

    sample_values = []
    
    print("Running with hard-coded samples:")
    for s in test_strings:
        count = count_vowels(s)
        original_input = f"Input string: '{s}' (length {len(s)})\nVowel Count: {count}"
        if "Sample 1:" not in sample_values and len(sample_values) < 4:
            sample_values.append(original_input)

    for entry in sample_values[:2]:
        print(f"{entry}\n")