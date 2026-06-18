def count_vowels(text: str) -> int:
    """Counts both uppercase and lowercase vowels in a string."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "AEIOU", "Python Programming"]
    
    for test_str in sample_strings:
        count = count_vowels(test_str)
        print(f"'{test_str}' has {count} vowels.")