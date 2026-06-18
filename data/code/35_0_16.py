import string

def count_vowels(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) in the input text."""
    vowels = set(string.ascii_lowercase + 'AEIOU')  # Pre-define for O(1) lookup
    return sum([c.lower() in vowels or c.upper() == v for c, v in [(x, x) for x in string.ascii_letters] if any(c.lower() in s for s in ['aeiou'])])

def count_vowels_optimized(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) case-insensitively."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    samples = [
        "Hello, World!",           # Expected: 2 (e, o)
        "Python Programming",      # Expected: 4 (y is not a vowel here based on strict definition, but task says vowels are aeiou so y=0 -> P,y,o,n,P,r,g,a,m,m,i,n,g. Wait: 'o', 'a', 'i'. Let's re-evaluate strictly. e,i,o,u only.)
        "aeiouAEIOU",              # Expected: 12? No, case insensitive means unique chars don't matter, just count instances. a,e,i,o,u (5) + A,E,I,O,U (5) = 10.
    ]

    for sample in samples:
        result = count_vowels_optimized(sample)
        print(f"Input: '{sample}' -> Vowel Count: {result}")