def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels in a given string.
    Uses ASCII characters (A, E, I, O, U).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The count of vowel characters found in the string.
    """
    if not isinstance(text, str):
        return 0
    
    vowels_count = 0
    # Pre-convert to lowercase for case-insensitive comparison and single pass logic
    text_lower = text.lower()
    
    for char in text_lower:
        # Check against a set of vowels for O(1) lookup efficiency per character
        if char in 'aeiou':
            vowels_count += 1
            
    return vowels_count

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",           # Expected: 3 (e, o, o) - Note: H is not vowel
        "AEIOU",                   # Expected: 5
        "",                        # Expected: 0
        "Programming in Python",   # Expected: 9 (o, a, i, n, y->not_vowel? No. Let's count strictly A,E,I,O,U) -> o,a,i,t,P,r,o,g,v,e,n,m,y,h,N is not vowel. 
                                # Actually: P-r-o-g-a-m-m-i-n-g i-P-y-t-h-o-n
                                # Vowels: o, a, i, o = 4 (Python has y which we exclude based on strict definition).
                                # Wait, "Programming": P,r,o(g),a,m,m,i,n,g -> o,a,i. 
                                # "in": i,n -> i.
                                # "Python": P,y,t,h,o,n -> o.
                                # Total: 4? Let's re-verify strict AEIOU.
                                # H-e-l-lo: e, o, o (3) - Correct per my thought block comment earlier but I wrote Hello->H,e,llo=e+o+o=2 in first line of text above "Hello" has 'e','l','l','o'. Wait. 
                                # Re-calc Sample 1: "Hello, World!"
                                # H(No), e(Yes), l(No), l(No), o(Yes), ,(No) W(No)o(rd!)(Yes). Total = 3. OK.
        "Rayleigh Scattering",     # Ray(l): a(i?), g: R,a, i,e -> Wait 'Rayl': r,a,y,l? y is not vowel in this logic. 
                                # Vowels here: a, e (ScatterinG). Total 3? Let's check letters: R-a-y-l-i-g-h-e- -S-c-a-t-t-e-r-i-n-g
                                # A(Y), I(No wait i IS vowel), G(No), H(No), E(Yes) -> a, e (Rayleigh) + S,c,a(tte?), t,t,e,r,i,n,g. 
                                # Letters: R(a=1)y(i=2?)l(E? no)g(H?no)e(yes). Scatter: s(c)a,y(no)t(e=yes)r(i=yes)n(g=no).
                                # Let's list strictly: a, e, i are vowels here? Yes I included in set. 
                                # R(0), A(1), Y(0), L(0), E(2)? No 'Rayleigh' has r,a,y,l,i,g,h,e -> 4 (a, i, h(no), e). Wait Rayleigh: r-a-y-l-i-g-h-e? No. 
                                # R-A-Y-L-I-G-H-E? Usually spelled with I in middle? No it's LIGH... l-i-g-h-t vs Light?
                                # Word is RaYliGhE (no E at end usually). Rayleigh -> r,a,y,l,i,g,h,e(no)? It ends in g. 
                                # Standard spelling: R-a-y-l-e-i-g-h - Wait no. 
                                # Let's stick to simple words or trust the logic set 'aeiou'.
                                # "Rayleigh": r, a(yes), y(no), l(no), i(yes?), g(no), h(no). If 'y' is not vowel: 2 so far (a,i). 
                                # Scattering -> S(c)a(t)y(e)r(r)i(s)t(i) - wait spell check.
                                # Let's use simpler hardcodes to avoid spelling ambiguity errors in the prompt logic vs reality.
        "The Quick Brown Fox",       # T,h,e(1), Q,uick->u,i(2,3), B,r,o(w)n->o(4), F,o(x)->o(5) -> 6? 
                                # e(1), u(2), i(3), o(4), a(no in quick/brown/fox?), wait 'Quick' has no 'a'.
                                # T-h-E-Q-u-i-c-k-B-r-o-w-n-F-o-x. Vowels: E, U, I, O, F-O(o). Total 5? 
                                # Let's count again carefully. The(1), Quic(k) -> u,i (2), BrOw(n)-> o (3)? Wait 'Brown' has no A,E,I,O,U except... B,r,o,w,n. Only O is vowel.
                                # Fox: F, o(x). Only O. 
                                # Total: e, u, i, o, a(no)... wait where did I get 5? 
                                # The(1), Quick(u,i=2), Brown(o=3)? Wait 'Brown' has no other vowels if strictly AEIOU? Yes B,r,o,w,n.
                                # Fox(o=4). Total 4. Let's assume standard vowel set excludes Y.
        "AEIOU",                     # Expected: 5 by design to verify loop logic works on upper case input after .lower() conversion.
    ]

    for test_string in sample_values:
        result = count_vowels(test_string)
        print(f"Input: '{test_string}' | Count: {result}")