def count_vowels(text: str) -> int:
    """Counts the total number of vowels in the given string (case-insensitive)."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text if char.lower() in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    samples = [
        "Hello, World!",  # Expected: 3 (e, o, o)
        "Python Programming",  # Expected: 6 (y, t-h-n are not vowels? Wait: P-y-t-h-o-n -> y,o,n(no), Pr-o-g-r-a-m-m-i-n-g. Vowels: o, a, i. Let's re-evaluate carefully.)
    ]

    # Correct manual count for "Python Programming":
    # P - no
    # y - no (sometimes considered vowel sound but not in set {a,e,i,o,u}) -> Task specifies a,e,i,o,u only.
    # t - no
    # h - no
    # o - yes
    # n - no
    
    # r - no
    # o - yes
    # g - no
    # r - no
    # a - yes
    # m - no
    # m - no
    # i - yes
    # n - no
    # g - no
    # Total: 4 (o, o, a, i)

    sample1 = "Hello World"       # e, o, o -> 3
    sample2 = "AEIOUaeiou"        # all uppercase and lowercase vowels -> 10
    
    test_cases = [
        ("Hello World", 3),
        ("AEIOUaeiou", 10),
        "",                        # Edge case: empty string -> 0
        "bcdfghjklmnpqrstvwxz",   # No vowels -> 0,
        "The quick brown fox jumps over the lazy dog.", # t-h-e(1) q-u-i-c-k b-r-o-w-n f-o-x j-u-m-p-s o-v-e-r t-h-e l-a-z-y d-o-g. 
                   # e, u, i, o, a -> 5? Let's count: The(1), quick(u,i=2), brown(o=3), fox(jumps->u=4) over(o,v,e=5,6), the(e=7), lazy(a=8), dog(o=9). Total 9.
        ("The quick brown fox jumps over the lazy dog.", 9)
    ]

    for text, expected in test_cases:
        result = count_vowels(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{text}' -> Counted {result} (Expected {expected})")