#!/usr/bin/env python3
"""
Script to find repeated letters in a string.
This script is self-contained and requires no user input, command-line arguments, 
network access, or external files.

Usage: Run this file directly (e.g., 'python script.py'). It will execute the sample test case automatically.
"""

def find_repeated_letters(text):
    """
    Identifies letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list: A sorted list of unique repeated letters found in lowercase format.
              If no repetitions are found, returns an empty list.
              
    Example:
        >>> find_repeated_letters("Hello World!")
        ['e', 'h', 'l', 'o'] (Note order depends on first occurrence or sort)
        
        Actually, to ensure deterministic output regardless of input length/complexity, we will return a sorted list.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Dictionary to count occurrences of each letter (case-insensitive)
    letter_counts = {}
    
    for char in text:
        # Only consider alphabetic characters and convert to lowercase
        if 'a' <= char.lower() <= 'z':
            normalized_char = char.lower()
            letter_counts[normalized_char] = letter_counts.get(normalized_char, 0) + 1

    # Extract letters that have a count greater than 1
    repeated_letters = [char for char, count in letter_counts.items() if count > 1]
    
    # Sort the list to ensure consistent output regardless of input order
    return sorted(repeated_letters)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user prompts or interactive calls are used here.

    test_cases = [
        "Hello World!",          # Expected: ['e', 'h', 'l', 'o'] (sorted) -> Wait, logic check below
                            # H(1), e(2->repeat?), l(3), o(2)->'H','W','L','O'? Let's trace manually.
                            # "Hello World!" -> h,h? No. 
                            # Text: "hello world" (case insens)
                            # h: 2, e:1, l:3, o:2, w:1, r:1, d:1
                            # Repeats: h(2), l(3), o(2). Sorted: ['h', 'l', 'o']? 
                            # Wait "Hello": H,e,l,l,o. W,r,l,d (World) -> L is repeated 3 times total in string? Yes. O twice. E once.
                            # Let's re-verify trace for sample 1: "Hello World!"
                            # h, e, l, l, o, w, r, l, d -> counts: {h:2 if case insensitive? No 'H' is one, no other H in string unless specified. 
                            # Wait, standard interpretation of repeated letters usually implies same character value ignoring case.
                            # Input "Hello World!": chars are h,e,l,l,o,w,r,d (ignoring ! and space) + original casing doesn't matter for identity if we treat as set then count? Or strict char match? 
                            # Prompt says "repeated letters". Usually implies identical characters or same letter regardless of case.
                            # Let's assume Case Insensitive for robustness unless specified otherwise, but often these tasks imply exact matches first?
                            # Re-reading: "takes a string... checks for any repeated letters". 
                            # If I say "Apple", 'a' appears once (as A), 'p' twice. Is 'A' same as 'a'? Usually yes in linguistic contexts, but strictly it's different char codes.
                            # Given the ambiguity, Case Insensitive is the standard interpretation for "letters found" unless case-sensitivity is requested explicitly. 
                            # However, to be safe and robust against specific strict interpretations: Let's stick to lowercase normalization as done above logic.

        "Python Programming",    # p,y,t,h,o,n,r,g,a,m,i,n -> n repeats (1 in pytho, 2 in progra... wait Python has one n). 
                                # P-y-t-h-o-n- -P-r-o-g-a-m-m-i-n-g
                                # p:3 (Pyth**on**, **Pr**ogra**mming**) -> actually 'p' is at start. "Python" ends with n. "Programming".
                                # Let's count exactly: 
                                # P, y, t, h, o, N, -, P, r, o, g, a, m, M, i, n, g, - (spaces/hyphens?) No spaces in string above? Just letters and maybe space.
                                # String "Python Programming": 
                                # p: 1(P), y(2)? no. t,h,o,N,P,r,o,g,a,m,M,i,n,g.
                                # Case insensitive counts:
                                # P/p: 3 (P in Python, P in Progrrammng? No only one P). Wait "Python" -> P,y,t,h,o,n. "Programming" -> p,r,o,g,a,m,m,i,n,g. 
                                # Total lowercase: pyth on programmar mming -> n repeats (on...n). o(2), r(1?), g(3??), a(1)?
                                # Let's simplify the sample to avoid complex counting errors in my head and rely on code correctness.

        "Able was I ere I saw able", # 'a' appears many times, 'b', 'e' repeats heavily.
    ]

    all_repeated_letters = []  # List of sets for each test case (or just a single list if we process one by one)
    
    # Process samples sequentially to avoid printing in complex order or mixing results incorrectly? 
    # Actually, the prompt says "printing ALL repeated letters found". It doesn't specify format.
    # A clean way is: Print headers and then lists for each sample. Or just a single combined result from one string passed as argument of our choice inside main.
    # Let's define ONE primary test case to keep it simple and robust, or run through the list clearly.
    
    chosen_samples = [
        "Hello World!", 
        "A man is a man",       # 'a' appears 3 times (start, mid, end), 'm' twice? No m-i-s-a... m(1) i s a a n -> a repeats twice. M repeats once if case insensitive A=M? Yes.
                                # Case ins: "A"->a, "man"->ma,n. 
                                # String: A man is a man (length 14 chars including space).
                                # Chars: A,a,m,i,s,r,l,o... wait input string literal above had no 'r','l'. Just letters/space.
    ]

    for sample in chosen_samples:
        repeated = find_repeated_letters(sample)
        
        print(f"\nInput String: {sample}")
        if not repeated:
            print("No repeated letters found.")
        else:
            print(f"Repeated letters: {''.join(repeated)}") # Joining for compactness