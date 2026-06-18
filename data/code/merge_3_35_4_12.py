def count_vowels(strings):
    """
    Accepts a list of strings and returns a dictionary where:
        - keys are the original input strings,
        - values are the counts of vowels (a, e, i, o, u) in each string.
    
    Vowel counting is case-insensitive.

    :param strings: List of strings to analyze.
    :return: Dictionary mapping each string to its vowel count.
    """
    vowels = set("aeiouAEIOU")
    result = {}
    
    for s in strings:
        # Count occurrences of 'a', 'e', 'i', 'o', 'u' (case-insensitive)
        count = sum(1 for char in s if char.lower() in vowels)
        result[s] = count
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    samples = [
        "hello",
        "AEIOUaeiou",
        "",
        "rhythm",
        "creative"
    ]

    vowel_counts = count_vowels(samples)

    print("Vowel counts for the sample strings:")
    for string, count in vowel_counts.items():
        # Ensure output is clean (no trailing newline issues if needed, though standard print is fine here)
        print(f"'{string}': {count}")