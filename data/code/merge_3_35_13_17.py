def count_vowels(text: str) -> int:
    """Returns the total number of vowel characters (a, e, i, o, u) in the string."""
    vowels = set('aeiouAEIOU')
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "Python Programming",
        "",
        "AEIOUaeiou"
    ]
    
    for string in test_cases:
        print(f"'{string}': {count_vowels(string)}")