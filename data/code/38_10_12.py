import string

def find_repeated_letters(text: str) -> list[str]:
    """
    Returns a sorted list of letters that appear more than once in the input text.
    Only alphabetic characters (A-Z, a-z) are considered; numbers and symbols are ignored for counting but included if they repeat (though typically we focus on 'letters').

    The implementation:
    1. Filters only alphabetic characters to ensure strict letter checking as per standard interpretation of "repeated letters".
       If the requirement implies any character type, this can be adjusted, but usually "letter" means [a-zA-Z].
       To be safe and robust regarding case-insensitivity for identification while preserving original char:
       We will normalize to lowercase for counting to treat 'A' and 'a' as the same letter.
    2. Counts occurrences of each normalized character.
    3. Identifies characters with a count > 1.
    4. Returns them sorted alphabetically (case-insensitive order).

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of unique letters that are repeated in the input.
                   If case sensitivity is strictly required for output uniqueness, this logic can be tweaked;
                   here we group 'A' and 'a' as one letter type but return them consistently (lowercase).
       """
    # Filter to alphabetic characters only if strict definition of "letter" is desired.
    # If the user wants all repeated chars including numbers/symbols, replace this filter logic.
    letters = [ch for ch in text if ch.isalpha()]

    letter_counts: dict[str, int] = {}
    
    # Normalize to lowercase for counting 'A' and 'a' as the same entity
    for char in letters:
        count_key = char.lower()
        letter_counts[count_key] = letter_counts.get(count_key, 0) + 1

    repeated_chars = [key for key, count in letter_counts.items() if count > 1]

    # Sort alphabetically (already lowercase keys here)
    return sorted(repeated_chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "Hello, World!",      # Expected: ['e', 'l', 'o'] (case-insensitive unique letters repeated)
        "Python Programming",  # Expected: ['r', 'p'/'P' -> handled as one] -> actually P/p and r/r. Let's trace: p,P,r,o,g,p,r,a,m,m,i,n,g. Repeated: p, g, m, r, o? No wait.
                            # H e l l o , W o r l d !
                            # Python: P y t h o n -> no repeats in word itself except if combined with others.
                            # "Python Programming": 
                            # P,p : yes
                            # g,g : yes (from prog,gramming)
                            # m,m : yes
                            # r,r : yes
                            # o,o : yes? No only one 'o' in Python and Prog? Wait: Pro-gram-ming. One 'o'. 
                            # Let's re-count manually for "Python Programming":
                            # P, y, t, h, o, n (1 each)
                            # r, p, o, g, r, a, m, m, i, n, g
                            # Combined: P(2), y(1), t(1), h(1), o(2 - one in Python, one in Prog? Wait. Pro... yes 'o'. Programming has no second 'o'? 
                            # Actually "Programming": p-r-o-g-r-a-m-m-i-n-g. Only one 'o'.
                            # So 'P' and 'p' are the same letter repeated (count 2).
                            # 'r': r(Prog), r(gramming) -> count 2.
                            # 'g': g(prog), g(gramming) -> count 2.
                            # 'm': m(mmm? no, gram-ning has mm) -> count 2.
                            # So expected: ['p', 'g', 'r', 'm'] (sorted). 
        "Mississippi",         # Expected: ['i', 's', 'p'/'P'? No caps] -> s,s,i,p,m,o? Missis-sippi. m(1), i(s,si,sippi-> many), s(mississi-> 4?), p(pipi->2?). 
                            # M-i-s-s-i-s-s-i-p-p-i
                            # I: 5 times (repeated)
                            # S: 4 times (repeated)
                            # P: 2 times (repeated)
                            # Others once. Expected: ['i', 'p', 's'] sorted -> p, s? No alphabetical i, p, s. Wait I is before P and S? Yes. So ['i', 'p', 's'].
        "AaBbCc",              # All pairs repeated.
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}'")
        if not result:
            print("No repeated letters found.")
        else:
            print(f"Repeated letters: {result}")