def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a string, 
    case-insensitive and ignoring non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Python Programming",
        "",
        "AeIoU",
        "bcdfg"
    ]

    for test_input in sample_strings:
        result = count_vowels(test_input)
        print(f"'{test_input}' -> {result}")