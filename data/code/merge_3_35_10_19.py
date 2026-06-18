def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in the given string,
    ignoring case sensitivity and any other characters.
    
    Parameters:
        text (str): The input string to process.
        
    Returns:
        int: The count of vowel occurrences.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    samples = [
        "Hello, World!",
        "Python Programming",
        "aeiouAEIOU",
        "NoVowelsHere123",
        ""
    ]

    for test_string in samples:
        count = count_vowels(test_string)
        print(f"'{test_string}': {count} vowels")