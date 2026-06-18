class StringProcessor:
    def count_vowels(self, text: str) -> int:
        """
        Counts the number of vowels in the given string (both uppercase and lowercase).
        
        Time Complexity: O(n), where n is the length of the input string.
        Space Complexity: O(1).
        
        Args:
            text (str): The input string to process.
            
        Returns:
            int: The count of vowels found in the string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        vowel_set = set('aeiouAEIOU')
        count = 0
        
        # Iterate through each character exactly once for O(n) traversal
        for char in text:
            if char in vowel_set:
                count += 1
                
        return count

if __name__ == '__main__':
    sample_1 = "Hello, World!"
    result_1 = StringProcessor().count_vowels(sample_1)

    sample_2 = "Programming is fun."
    result_2 = StringProcessor().count_vowels(sample_2)

    print(f"Vowel count for '{sample_1}': {result_1}")  # Expected: 3 (o, o, a -> actually 'H','e','l','l','o' is 2 + ',' skip + space + W,o,r,l,d -> O,I,O = let's trace manually)
    # Trace sample_1 "Hello, World!": e(yes), l(no), l(no), o(yes), ,(no), (space)(no),W(no),o(yes),r(no),l(no),d(no),(no)! => 3 vowels? No. 'e', 'o' in Hello = 2. 'o' in World = 1. Total 3. Wait, 'a'? None. Correct is 3.
    
    # Re-trace carefully:
    # H - no
    # e - yes (1)
    # l - no
    # l - no
    # o - yes (2)
    # , - no
    # space - no
    # W - no
    # o - yes (3)
    # r - no
    # l - no
    # d - no
    # ! - no
    # Total 3.

    print(f"Vowel count for '{sample_2}': {result_2}")
    
    # Trace sample_2 "Programming is fun."
    # P-no, r-no, o-yes(1), g-no, n-no, a-yes(2), m-missing? No 'm'. i-yes(3), n-n-o. Wait spelling: P-r-o-g-r-a-m-m-i-n-g space i-s space f-u-n-.-
    # P r - no 
    # o - yes (1)
    # g
    # r
    # a - yes (2)
    # m
    # m
    # i - yes (3)
    # n
    # g
    
    # space    
    # i - yes (4)
    # s
    
    # space
    
    # f-u-n -> u is vowel. Yes(5).
    # .
    # Total 6? Let's recheck "Programming". o, a, i = 3. "is" = 1 ("i"). "fun" = 1 ("u"). Total 5.
    # Wait, P-r-o-g-r-a-m-m-i-n-g (o,a,i) -> 3. is(i)->4. fun(u)->5. 
    # Let's re-read sample_2: "Programming is fun."
    # o - yes
    # a - yes
    # i - yes
    # space
    # i - yes
    # u - yes (f-u-n)
    # Total 5.

    print(f"Sample results computed successfully.")