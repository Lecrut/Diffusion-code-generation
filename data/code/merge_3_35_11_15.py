def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a string, case-insensitive.
    
    This implementation is optimized by using a set for constant-time lookups
    and iterating through the input characters directly without converting 
    the entire string to lowercase unless necessary per character (handled via conditional).

    Args:
        text (str): The input string to analyze. Non-alphabetic characters are ignored.

    Returns:
        int: The count of vowels ('a', 'e', 'i', 'o', 'u' or their uppercase equivalents) in the string.
    
    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_set_uppercase = {v.upper() for v in vowels}
    
    count = 0
    
    # Direct iteration avoids creating intermediate lists or strings.
    for char in text:
        if char.lower() in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required.
    samples = [
        "Hello, World!",           # Expected: 2 (e, o) - Note: 'o' in world is vowel, 'e' in hello
        "AEIOUaeiou123",          # Expected: 10
        "",                        # Expected: 0
        "Rhythm is yhat.",         # Expected: 4 (i, a vowels? No. i, o(no), h(yh)at -> a,t no. Wait: R-y-t-h-m-i-s-y-h-a-t. Vowels: i, a. Count=2.) Let's re-evaluate common English words usually tested.
        "Python Programming",      # Expected: 6 (y is sometimes considered but standard definition excludes it here based on strict 'a,e,i,o,u'. P,y,t,h-o-n,P-r-o,g-r-a-m-m-i-n-g -> o, o, a, i = 4? Let's stick to strict A,E,I,O,U.)
    ]

    # Correction for samples above strictly using {a, e, i, o, u}:
    sample1 = "AEIOUaeiou"       # 10 vowels
    sample2 = "Python Programming" # p,y,t,h,o,n,p,r,g,a,m,m,i,n,g -> o, a, i (3) + 'o' in programming? P-y-t-h-o-n(1), P-r-o-g-r-a-m-m-i-n-g(o=2, a=3, i=4). Total 4.
    sample3 = "The quick brown fox jumps over the lazy dog" # t,h,e(1) q,u(i,o,y,j,m,p,s)o,v,t,h-e(5)i,n,i,g,z,a,d -> e,q(u),i,c,k,b,r,o,w,f,x,J(m)p(s, o=6? 'o' in brown/fox/jumps/over/lazy/dog). Let's simplify samples to avoid ambiguity.
    
    # Final Simplified Samples for clarity and correctness:
    test_cases = [
        "Hello",                  # e, o -> 2
        "AeioUaEIoU",            # 8 (4 upper + 4 lower)
        "Rhythm is yhat.",       # i, a -> 2 (Strictly A,E,I,O,U only. 'y' and 'h', 't' are not vowels). Wait: R(y)t(h)m(i)s(y)(h)a(t). Vowels: i, a. Count=2.
        "12345",                 # 0
        "",                      # 0
    ]

    for text in test_cases:
        result = count_vowels(text)
        print(f"Input: '{text}' -> Count of vowels: {result}")