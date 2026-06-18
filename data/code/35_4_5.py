def count_vowels(input_strings):
    """
    Accepts a list of strings and returns a dictionary where:
        - Keys are the input strings themselves (as they were provided).
        - Values are the counts of vowels in each string.
    
    Vowels considered: 'a', 'e', 'i', 'o', 'u' (case-insensitive).

    Args:
        input_strings (list[str]): A list of strings to analyze.

    Returns:
        dict: Mapping from original string to its vowel count.
    """
    vowels = set("aeiouAEIOU")
    
    result = {}
    for s in input_strings:
        # Count occurrences of any vowel character in the string
        vowel_count = sum(1 for char in s if char in vowels)
        result[s] = vowel_count
    
    return result

if __name__ == '__main__':
    # Sample data - no user input required
    sample_data = [
        "hello",
        "aeiou",
        "rhythm",
        "",
        "Python is great!"
    ]

    output = count_vowels(sample_data)

    print("Input-Output Pairs:")
    for key, value in output.items():
        print(f"Key: '{key}' -> Vowel Count: {value}")