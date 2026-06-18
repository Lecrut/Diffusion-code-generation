def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    The function is case-sensitive and considers both uppercase and lowercase 
    as distinct characters unless specified otherwise (standard behavior).
    Non-letter characters are ignored based on the requirement to return 'letters'.

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set of unique letters that appear more than once in the string.
    
    Example:
        >>> find_repeated_letters("hello world")
        {'l', 'o'}  # Note: 'e' appears once, 'w','r','d','H'(if present) etc. check carefully
    
    Optimization Strategy:
        - Use a dictionary (hash map) to count occurrences of each character in O(n) time complexity.
        - Iterate through the string only once.
        - Filter characters with a count greater than 1 at the end or during iteration.
    
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(k), where k is the number of unique characters in the string.
    """
    char_count = {}

    for char in text:
        # Check if the character is a letter (a-z, A-Z) to strictly follow "letters" requirement
        if 'a' <= char.lower() <= 'z':
            count = char_count.get(char, 0) + 1
            char_count[char] = count

    repeated_letters = {char for char, count in char_count.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "hello world",      # Expected: {'l', 'o'} (case sensitive) -> actually 'h','e','l','o','w','r','d'. l appears twice, o appears once? Wait: h-1, e-1, l-2, o-1, w-1, r-1, d-1. So only 'l'? No wait "hello": l is 2nd and 3rd char. 'o' is last in hello. Then space. Then world. o again? Yes.
        # Let's trace: h(1), e(1), l(2), l(3->count=2), o(4->count=1), _(0), w(5->1), r(6->1), d(7->1). 
        # Wait "hello": h,e,l,l,o. Counts: h:1, e:1, l:2, o:1.
        # "world": w,r,o,l,d. Counts added: w:1, r:1, o:total 2 (from hello+world), l:total 3 (hello+world). d:1.
        # So repeated should be 'l' and 'o'. 
        # Correction on manual trace above in comment logic vs code execution later. Code is correct.
        
        "aabbc",             # Expected: {'a', 'b'}
        "abcdefg",           # Expected: set() (no repeats)
        "",                  # Expected: set() (empty string)
        "A man a plan",     # Case sensitive? If case-sensitive, A and a are different. 
                           # h-1, m-2, n-1, p-1, l-1, r-1, s-1. 'm' is repeated. Also spaces ignored by letter check.
        "Python Programming",# P,y,t,h,o,n (all 1), P(again)->P:2. 
                           # Wait: Python -> P:y:t,h:o,n. Prog -> p,r,g,p,i,n,m? No, let's look at string literal carefully.
                           # String is "Python Programming". 
                           # 'P' appears twice (start and after space). 'r','o','g','p','i','n','m'.
                           # Actually standard lowercase/uppercase distinction usually applies unless told otherwise.
                           # If case insensitive: p,P are same? The problem says "letters", doesn't explicitly say case-insensitive. 
                           # Standard set logic is often case-sensitive by default in Python strings. 
                           # However, for natural language tasks, sometimes it implies ignoring case. 
                           # Given the instruction "optimized function... efficient data structures" without specifying normalization,
                           # strict character matching (case-sensitive) is the safest interpretation of a generic string task unless specified.
                           # But let's re-read: "all letters". Usually in such puzzles, if not specified, it might be ambiguous. 
                           # Let's stick to case-sensitive as implemented by `char` directly from loop.
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}' -> Output: {result}")