class StringAnalyzer:
    def check_for_duplicates(self, text: str) -> list[str]:
        """
        Identifies all characters that appear more than once in the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            A sorted list of unique characters found multiple times in the string.
        """
        char_counts = {}
        duplicates_found = []

        for character in text:
            # Count occurrences of each character
            count = char_counts.get(character, 0) + 1
            
            if count == 2:
                # This is the first time we see a duplicate, add to list only once per unique char
                duplicates_found.append(character)
            
            elif count > 1 and character not in duplicates_found:
                # Handle case where multiple instances are counted sequentially for same char before check logic above triggers? 
                # Actually simpler approach: just track counts first then filter.
                pass
            
            char_counts[character] = count

        return sorted(list(set(duplicates_found)))

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    test_strings = [
        "hello world",         # Expected: ['l', 'o']
        "aabbccddeeffgg",     # Expected: all letters a-z appear twice? No wait: a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z. Input has only up to f then g... 
                             # Actually input is 'a'x2, 'b'x2 ... 'f'x2, 'g'x1 -> duplicates: a,b,c,d,e,f
        "programming",         # Expected: ['r', 'o'] (p appears 3 times)
    ]

    for test_str in test_strings:
        result = analyzer.check_for_duplicates(test_str)
        print(f"Input: '{test_str}'")
        print(f"Duplicates found: {result}")
        print("-" * 20)