def count_vowels(text: str) -> int:
    """Return the number of vowel characters (a, e, i, o, u) in the string."""
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "AEIOUaeiou",
        "",
        "Rhythm",
        "Programming is fun!"
    ]
    
    results = []
    for s in sample_strings:
        count = count_vowels(s)
        results.append(f"String: '{s}' -> Vowel Count: {count}")

    print('\n'.join(results))