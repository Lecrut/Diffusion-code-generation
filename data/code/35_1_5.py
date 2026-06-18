def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string using a single loop.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowels found in the string.
    """
    if not isinstance(text, str):
        return 0
    
    vowel_set = set("aeiouAEIOU")
    count = 0
    
    for char in text:
        if char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        "Hello, World!",
        "aeiouAEIOU",
        "",
        "Python Programming",
        "xyz"
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"'{sample}' -> {result}")