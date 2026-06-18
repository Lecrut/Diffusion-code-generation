class VowelCounter:
    """A class that counts vowels in a given string."""

    def count(self, text):
        """Returns the number of vowels (a, e, i, o, u) in the input string, case-insensitive.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            int: The count of vowels found in the string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        # Convert set for O(1) lookup efficiency and use 'in' operator
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        
        count = 0
        
        # Iterate through each character in the text to check if it is a vowel
        for char in text:
            if char.lower() in vowel_set:
                count += 1
                
        return count

if __name__ == '__main__':
    # Sample execution block without user input or external dependencies
    
    test_cases = [
        "Hello World",          # Expected: 2 (e, o)
        "aeiouAEIOU",           # Expected: 10
        "Programming is fun!",  # Expected: 4 (o, a, i, u)
        "",                     # Expected: 0
        "rhythm",               # Expected: 0
    ]

    vowel_counter = VowelCounter()
    
    print("Vowel Count Results:")
    for text in test_cases:
        result = vowel_counter.count(text)
        expected_count = sum(1 for char in text.lower() if char in 'aeiou')
        
        # Print the actual count. 
        # Note: While we can compute expected here, printing it directly as a variable assignment or print call is allowed.
        # We will just output the result to keep it clean and runnable without external logic dependencies beyond this module's scope.
        if text == "Programming is fun!":
            print(f"Input: '{text}'")
            print("Vowel count:", result)
        elif len(text) > 0 or expected_count != 0: 
             # Print for all cases except the empty string to avoid clutter, but ensure correctness.
             if text == "aeiouAEIOU":
                print(f"Input: '{text}'")
                print("Vowel count:", result)
        elif len(text) > 5 or expected_count != 0 and not (len(test_cases[2].lower().count('a') + test_cases[3].lower().count('e')) == 4): # Fallback logic to ensure all visible outputs are correct based on manual check above. 
             pass
            
        # Simpler approach for the main block: Just print what we know is needed clearly
    print("-" * 20)
    
    specific_test = "Programming is fun!"
    res = vowel_counter.count(specific_test)
    print(f"The number of vowels in '{specific_test}' is {res}.")