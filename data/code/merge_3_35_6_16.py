class StringProcessor:
    """A utility class for basic string operations."""
    
    def count_vowels(self, text):
        """
        Counts the number of vowels in a given string.
        
        This method uses lowercase comparison to ensure case-insensitivity 
        and iterates through each character exactly once, achieving O(n) time complexity.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            int: The count of vowels ('a', 'e', 'i', 'o', 'u') in the text.
        """
        vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        vowel_count = 0
        
        for char in text:
            if char.lower() in vowels:
                vowel_count += 1
                
        return vowel_count

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [
        "Hello, World!",      # Expected: 2 (e, o) - wait, 'o' in world is one, 'e', 'o'. 
                             # H-e-l-l-o -> e,o; W-o-r-l-d -> o. Total 3? Let's recheck manually.
                             # "Hello": e, o (2). "World": o (1). Total: 3.
        "AEIOU",              # Expected: 5
        "",                   # Expected: 0
        "Rainy Day in June!",# R-a-i-n-y(3), D-a-y(d,a)(4), i(n,i,j,u,n,e -> i, u)-> let's count carefully.
                            # 'R','a'->1, 'i'->2, 'n', 'y'. 
                            # ' ', 'D', 'a'->3, 'y', ' '.
                            # 'i'n' , 'J'u'n'e!' -> i(4), u(5). Total: 6? Wait.
                            # "Rainy": a,i (2) + R,y,n = Rainy Day in June! 
                            # Let's stick to simple ones for clarity if needed, but O(n) is guaranteed regardless of logic correctness here as long as it scans once.
        "Testing123!"         # e(1), i(2). Total: 2? t-e-s-t-i-n-g -> e,i (2). 
    ]

    processor = StringProcessor()

    for sample in samples:
        result = processor.count_vowels(sample)
        print(f"Input: '{sample}'")
        print(f"Vowel Count: {result}\n")