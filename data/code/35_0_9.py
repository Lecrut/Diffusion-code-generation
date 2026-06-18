def count_vowels(text: str) -> int:
    """Counts the total number of vowels in a given string (case-insensitive)."""
    return sum(1 for char in text if char.lower() in "aeiou")

if __name__ == '__main__':
    # Hard-coded sample strings without user input or command-line arguments.
    sample_1 = "Hello, World!"
    sample_2 = "AEIOU aeiou"
    
    print(f"Sample 1: '{sample_1}' -> Count: {count_vowels(sample_1)}")
    print(f"Sample 2: '{sample_2}' -> Count: {count_vowels(sample_2)}")