def count_vowels(text: str) -> int:
    """
    Returns the total number of vowel characters in the input string,
    handling both uppercase and lowercase letters using a generator expression.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowels ('a', 'e', 'i', 'o', 'u' case-insensitive).
    """
    return sum(1 for char in text if char.lower() in "aeiou")

if __name__ == '__main__':
    # Hard-coded sample values; no user input or external dependencies required.
    samples = [
        "Hello, World!",
        "AEIOU",
        "Python Programming 2024",
        "",
        "aeiouAEIOU"
    ]

    for s in samples:
        print(f"'{s}' -> {count_vowels(s)} vowels")