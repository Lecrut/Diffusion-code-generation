def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string.
    The check is case-insensitive.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowel characters found in the string.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the entire string to lowercase for case-insensitive comparison,
    # then iterate through each character and check if it exists in our set.
    return sum(char.lower() in vowels for char in text)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "aeiouAEIOU",
        "",
        "Python Programming 101"
    ]

    for test_input in sample_strings:
        count = count_vowels(test_input)
        print(f"Input: '{test_input}'")
        print(f"Vowel Count: {count}")