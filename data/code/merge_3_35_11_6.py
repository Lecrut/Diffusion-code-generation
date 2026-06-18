def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a string,
    ignoring case and non-alphabetic characters efficiently using a set.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowel characters found.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Using sum with a generator expression for memory efficiency and readability.
    # This avoids creating an intermediate list, which is beneficial for large strings.
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "AEIOUaeiou",
        "Python3 Programming!",
        "NoVowelsHere####",
        ""
    ]

    for test_case in sample_strings:
        result = count_vowels(test_case)
        print(f"'{test_case}' -> {result}")