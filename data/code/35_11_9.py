def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a given string,
    case-insensitive and ignoring non-alphabetic characters.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: Total count of vowel characters found.
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "Hello World!",           # Expected: 2 (e, o)
        "Python Programming",     # Expected: 4 (y is not vowel here based on strict aeiou, but let's check logic. 'o', 'i' -> actually 3? y vs i/o/u/a/e strictly defined in set above. Let's trace: P-y-t-h-o-n... e- - p-r-o-g-r-a-m-m-i-n-g. Vowels: o, a, i. Count=4 if we count all occurrences? Wait: Python(0), Pr(o)1, ogr(a2)m(m)i3n(g). That's 3 in 'Programming'. Plus 'o' in 'Python'? No, y is not vowel here unless specified. Let's stick to strict aeiou.)
        "AEIOU",                  # Expected: 5 (all uppercase vowels)
        "",                      # Expected: 0
        "aeiou"                   # Expected: 5
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"'{sample}' -> {result} vowel(s)")