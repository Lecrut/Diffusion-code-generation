def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    Only alphabetic characters (both uppercase and lowercase) are considered,
    treating 'A' and 'a' as distinct unless specified otherwise based on standard
    interpretation where case matters for identity but we count occurrences per character instance.
    If the requirement implies case-insensitivity, it should be noted; however, 
    strictly speaking, in Python strings, 'A' != 'a'. This implementation counts exact matches.

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set of characters that appear more than once in the string.
    
    Example:
        >>> find_repeated_letters("hello")
        {'l', 'o'} -> Wait, 'h','e' are unique? No, h=1, e=2, l=3 (twice), o=4. So {l}. 
        Correction for "hello": h(1), e(1), l(2), o(1) -> {'l'}
        For "aabbcc": a(2), b(2), c(2) -> {'a', 'b', 'c'}
    """
    letter_counts = {}

    for char in text:
        # Ensure we are only processing alphabetic characters if desired, 
        # but the prompt says "letters", implying non-alphabetic might be ignored or included?
        # Usually "letters" implies [a-zA-Z]. Let's filter to ensure correctness.
        if not ('a' <= char.lower() <= 'z'):
            continue
        
        letter_counts[char] = letter_counts.get(char, 0) + 1

    repeated_letters = {char for char, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        "hello world",      # Expected: {'l', 'o'} (h=1, e=1, l=2, w=1, r=1, d=1) -> Wait, space ignored? Yes. 
                           # h(1), e(1), l(3 in hello+world?), o(4), ...
                           # "hello": h,e,l,x2,o -> {'l'}
                           # "hello world": h,e,l x3 (h-e-llo + w-o-rld? no, l is 3rd char of hello, 1st word. 
                           # Let's trace: h(1), e(1), l(2 in hello) + o(1). Then space ignored.
                           # "world": w,o,r,l,d -> l becomes count+1=3? No, 'l' is unique in world too? 
                           # Actually "hello" has two 'l's. "world" has one 'l'. Total 3 'l's. So {'l'} still?
                           # Wait, let's re-evaluate input carefully:
                           # Input: "hello world"
                           # h:1, e:1, l:2 (from hello), o:1 (from hello) -> then space ignored. 
                           # w:o:r:l:d -> wait 'o' is in word? Yes. So o count increases to 2.
                           # r:1, d:1.
                           # Final counts: h(1), e(1), l(3), o(2), w(1), r(1), d(1). 
                           # Repeated: 'l', 'o'. Correct.
        "aabbcc",           # Expected: {'a', 'b', 'c'}
        "programming",      # p,r,o,g,a,m,i,n (all 1 except? n is at end, m before it. g once. 
                           # Let's count manually: p(1), r(2 - twice in progra... no prog-ramming: p-r-o-g-r-a-m-m-i-n-g
                           # p:1, r:2 (prog + ram? No, prog-r-am-ming -> r is 2nd and 5th char. Yes.), 
                           # o(1), g(3 - progra... no, prog-ramming has g at end too?), a(1), m(4 - ammm? no, mm in middle), i(1), n(1).
                           # Actually: p,r,o,g,r,a,m,m,i,n,g. 
                           # r appears twice (indices 1 and 5 if 0-based: progra... wait prog-r-a-m-m-i-n-g -> index 4 is 'r'? No, p-0, r-1, o-2, g-3, r-4? Yes. a-5, m-6, m-7, i-8, n-9, g-10.)
                           # So r:2, m:2 (indices 6 and 7), g:3 (indices 3, 10). 
                           # Repeated: {'r', 'm', 'g'}.
        "The quick brown fox jumps over the lazy dog", # Case sensitive? Yes. 'T' != 't'. 'h' appears twice ('Th'e and ...the').
                # Let's assume case-sensitive as per standard string logic unless specified otherwise. 
                # If case-insensitive, it would be different. The prompt doesn't specify case handling explicitly other than "letters".
                # Standard interpretation: exact character match.
        ]

    for sample in samples:
        result = find_repeated_letters(sample)
        print(f"Input: '{sample}' -> Output: {result}")