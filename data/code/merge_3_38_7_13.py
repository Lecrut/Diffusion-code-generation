def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a list of unique letters that appear at least twice in the input string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    The order of returned letters is not guaranteed to be sorted or based on first occurrence.

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A list of unique uppercase/lowercase characters found more than once.
                   Note: To ensure uniqueness and consistent output, the result below 
                   is converted to lowercase in implementation for canonical comparison,
                   but returns them as they appear conceptually (normalized).
        
       Correction based on typical expectation for "unique letters": Return a list of unique identifiers.
    """
    # Normalize input to lowercase for case-insensitive processing
    normalized_text = text.lower()
    
    letter_count = {}
    
    # Count occurrences of each character in the normalized string
    for char in normalized_text:
        if not char.isalpha():  # Ignore non-alphabetic characters based on "letters" context, 
                               # though problem says "string", usually implies alphabetic focus.
             continue
        
        letter_count[char] = letter_count.get(char, 0) + 1
    
    # Collect letters that appear at least twice
    duplicate_letters = []
    
    for char in normalized_text:
        if not char.isalpha():
            continue
            
        count = letter_count[char]
        if count >= 2 and char not in duplicate_letters:
            duplicate_letters.append(char)

    return duplicate_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure module runs without user input or files.
    test_cases = [
        "Hello World",      # Expected: ['h', 'l', 'o'] (normalized logic, let's trace carefully)
                          # H->1, e->2, l->3+4=5? No wait. 
                          # String: Hello World -> h,e,l,o, ,w,o,r,l,d
                          # Lowercase: hello world
                          # Counts: h:1, e:1, l:3 (indices 2,7 in original, but lower at 2,4), o:2, w:1, r:1, d:1. 
                          # Wait "Hello": H,h,e,l,o," World": W,w,o,r,l,d
                          # Lowercase sequence: h e l l o   w o r l d
                          # Counts: h=1, e=1, l=3 (ll in Hello + l in world), o=2 (one in hello one in world), 
                          # Wait "Hello" has two 'l's? H-e-l-l-o. Yes. "World": W-o-r-l-d. One 'l'. Total 3 'l's.
                          # So duplicates: l, o. Result should be ['l', 'o'] if iterating and checking existence.
        "A man a plan",     # A:2 (case insensitive), m:1, n:1, p:1, l:1, a:nan? 
                          # Text: "A man a plan" -> lower: "a man a plan"
                          # Counts: a:3 (start, 'man', 'plan'), m:1, n:2 ('nan' part), space ignored.
                          # Duplicates: a, n. Result ['a', 'n'].
        "Programming",       # P,r,o,g,a,m,m,i,n,g -> p:r:o:g:a:m(2):m:i:n:g(2)g? 
                          # Wait Prog ram ming
                          # Letters: p,r,o,g,r,a,m,m,i,n,g
                          # Counts: r=2, o=1, g=3 (p-r-o-g-**r**-a-m-m-i-n-**g** -> wait "Programming" spelling)
                          # P-r-o-g-r-a-m-m-i-n-g. 
                          # p:1, r:2, o:1, g:2, a:1, m:2, i:1, n:1.
                          # Duplicates: r, g, m. Result ['r', 'g', 'm'].
        "racecar"            # All duplicates except... all appear twice? 
                          # r,a,c,e,c,r -> r=2, a=1, c=2, e=1.
                          # Duplicates: r, c.
    ]

    for test_input in test_cases:
        result = find_duplicate_letters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Duplicate letters: {result}")
        
        # Ensure the output format is consistent (lowercase list of unique chars)