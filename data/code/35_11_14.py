def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in the input string, case-insensitive.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        int: Total count of vowel characters ('a', 'e', 'i', 'o', 'u').
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [
        "Hello, World!",  # Expected: 2 ('e', 'o')
        "aeiou",          # Expected: 5
        "",               # Expected: 0
        "Biology is fun.", # Expected: 4 (i, o, i, u)
    ]

    for sample in samples:
        count = count_vowels(sample)
        print(f"'{sample}' -> {count}")