def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word."""
    if not isinstance(word, str):
        return 0
    
    vowels = "aeiouAEIOU"
    
    # Use generator expression for memory efficiency with large strings
    count = sum(1 for char in word if char in vowels)
    
    return count

if __name__ == '__main__':
    sample_words = ["hello", "world", "beautiful"]
    
    print("Vowel Count Results")
    print("-" * 30)
    
    for test_word in sample_words:
        result = count_vowels(test_word)
        print(f"'{test_word}': {result}")