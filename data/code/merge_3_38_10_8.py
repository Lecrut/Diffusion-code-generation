def find_repeated_letters(text: str) -> set:
    """
    Identifies all letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set of unique repeated letters found in lowercase.
    """
    letter_counts = {}
    
    # Iterate over each character in the string
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            lower_char = char.lower()  # Convert to lowercase for case-insensitivity
            
            # Increment count only if it's not already counted (avoids duplicates during first pass)
            # Actually, we need counts regardless of previous state in this loop logic.
            # Let's simplify: just increment every time and check at the end or use a set directly.
            
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 0
                
    # Collect letters where count is greater than 1
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments.
    samples = [
        "Hello World!",           # Expected: h, l (case-insensitive) -> {'h', 'l'}
        "Python Programming",     # Expected: p, r, o, g, a? Let's trace: P->p(1), y(1), t(1), h(1), o(2), n(3),  ,P->p(2)... 
                                # Wait, 'o' appears twice (Python Pro... no Python PrOgramming).
                                # p-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g
                                # Lowercase: p,y,t,h,o,n,p,r,o,g,r,a,m,m,i,n,g
                                # Counts: 
                                # p: 2 (Python, Pro...) -> Yes
                                # y: 1
                                # t: 1
                                # h: 1
                                # o: 2 (Pytho**n**, Pr**o**gramming) -> Wait. Python(1), Programming(2). 
                                # Actually "Programming" has one 'o'. "Python" has one 'o'. Total 2. Yes.
                                # r: 2 (Pro, Prog) -> Yes
                                # g: 2 (Prog, prog) -> No wait. P-r-o-g-r-a-m-m-i-n-g. One 'g' at index 5? 
                                # Let's re-index: p(0)y(1)t(2)h(3)o(4)n(5),p(6)r(7)o(8)g(9)r(10)a(11)m(12)m(13)i(14)n(15)g(16).
                                # 'o' at 4 and 8. Count=2.
                                # 'r' at 7 and 10. Count=2.
                                # 'm' at 12, 13 -> Count=2.
                                # 'n' at 5, 15 -> Count=2.
                                # 'g' at 9, 16 -> Count=2.
                                # So: p, o, r, m, n, g.
        "aabbcc",                 # Expected: a, b, c
        "The quick brown fox jumps over the lazy dog.",    # Standard pangram check usually unique except 'e' often repeated? 
                                                                # T-h-e-q-u-i-c-k-b-r-o-w-n-f-o-x-j-u-m-p-s-o-v-e-t-h-e-l-a-z-y-d-o-g
                                                                # e: 3 (The, the) -> Yes. o: 2 (brown, fox no f-o-x? brown has o, over has o). 
                                                                # Let's check 'e': The(1), over(2), the(3). Count=3.
    ]

    for sample in samples:
        result = find_repeated_letters(sample)
        if not result:
            print(f"No repeated letters found in: '{sample}'")
        else:
            # Sort the set to ensure consistent output order for verification, though sets are unordered by definition.
            sorted_result = sorted(result)
            print(f"Repeated letters in '{sample}': {sorted_result}")