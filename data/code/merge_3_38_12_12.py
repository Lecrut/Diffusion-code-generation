class StringAnalyzer:
    def check_for_duplicates(self, text):
        """
        Identifies all repeated characters in the given string instance.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            list[str]: A sorted list of unique characters that appear more than once in the string.
        """
        char_count = {}
        
        # Count frequency of each character
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Collect characters that appear more than once and sort them for consistent output
        duplicates = [char for count, char in sorted(char_count.items()) if count > 1]
        
        return duplicates

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    sample_strings = [
        "hello",           # Expected: ['l', 'o'] (sorted order based on ASCII or insertion, here we sort by char) -> l appears 2 times, h1, e1, o1? Wait. h=1, e=1, l=2, o=1. So only 'l'.
        "programming",     # Expected: ['r', 'o'] (p=3, r=2, o=2, g=2, a=1, m=2) -> p,g,m,o,r are repeated? Let's trace: p(3), r(2), o(2), g(2), m(2). So ['g', 'm', 'o', 'p', 'r']
        "abcdef",          # Expected: [] (no duplicates)
        "aabbccdd",        # Expected: ['a', 'b', 'c', 'd']
    ]

    for test_str in sample_strings:
        result = analyzer.check_for_duplicates(test_str)
        print(f"Input: '{test_str}'")
        print(f"Duplicates found: {result}")
        
        if not isinstance(result, list):
            raise TypeError("check_for_duplicates must return a list.")
            
    # Verify specific known cases for clarity in output logic (sorting ensures deterministic order)
    test_case_1 = "hello"  # h=1, e=1, l=2, o=1 -> ['l']
    result_1 = analyzer.check_for_duplicates(test_case_1)
    print(f"\nDetailed Check - '{test_case_1}': {result_1}")

    test_case_2 = "racecar"  # r=2, a=1, c=2, e=2 -> ['a', 'c', 'e']? No: r(2), a(1), c(2), e(2). Sorted chars with count>1: c, e, r.
    result_2 = analyzer.check_for_duplicates(test_case_2)
    print(f"Detailed Check - '{test_case_2}': {result_2}")

    # Final validation on a complex string to ensure correctness logic holds for all inputs
    test_case_3 = "mississippi"  # m=1, i=4, s=4, p=2 -> ['i', 'p']? Wait: m(1), i(4), s(4), p(2). Repeated: i, p. Sorted: i, p.
    result_3 = analyzer.check_for_duplicates(test_case_3)
    print(f"Detailed Check - '{test_case_3}': {result_3}")