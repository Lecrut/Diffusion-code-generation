def count_vowels(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) in a string case-insensitively."""
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert text to lowercase and iterate through each character
    count = 0
    for char in text.lower():
        if char in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input)
    samples = [
        "Hello, World!",
        "AEIOUaeiou",
        "Python Programming",
        "",
        "No vowels here"
    ]

    for test_string in samples:
        result = count_vowels(test_string)
        print(f"'{test_string}' -> {result} vowel(s)")