class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        """
        Identifies all repeated characters in a given string efficiently.
        
        Args:
            input_string (str): The string to analyze.
            
        Returns:
            list[str]: A sorted list of unique characters that appear more than once 
                      in the input string. Non-alphabetic characters are ignored unless 
                      explicitly requested; however, based on standard linguistic analysis 
                      expectations for 'characters', this implementation includes all Unicode code points 
                      but typically focuses on letters if non-letters create trivial duplicates (e.g., space).
                      
        Logic:
            - Traverse the string and count occurrences of each character.
            - Filter counts to only those greater than 1.
            - Return sorted unique characters for deterministic output.
            
        Note: This implementation handles all Unicode characters but focuses on meaningful repetition 
              (e.g., spaces, punctuation) which are technically duplicates in a technical sense unless 
              specified otherwise. If strict 'letters' were needed, a filter would be added here.
        
        Example: "aabbc" -> ['a', 'b']
             Example: "hello world!" -> ['l', 'o', ' '] (ignoring case sensitivity issues if not handled)
        """
        # Dictionary to store character counts
        char_counts = {}

        for char in input_string:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        # Filter characters that have a count greater than 1 and sort them alphabetically (case-sensitive)
        duplicates = [char for char, count in char_counts.items() if count > 1]
        return sorted(duplicates)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or arguments used.
    
    test_cases = [
        "hello world",
        "aabbccdd",
        "programming is fun",
        "aaaaabbbbccccddddeeeee",
        "1234567890"  # Expected: None as all are unique in this string without repetition unless counting digits carefully. 
                     # Actually '1','2'...'0' appear once, so empty list expected. Let's adjust to have repeats for clarity if needed, 
                     # but per spec we just run it.
    ]

    analyzer = StringAnalyzer()
    
    print("Repeated characters analysis:")
    print("-" * 30)
    
    for test_string in test_cases:
        result = analyzer.check_for_duplicates(test_string)
        
        if not result:
            # Provide a fallback message when there are no duplicates 
            # to avoid printing "[]" which might look like an error or empty data to beginners.
            print(f"Input: '{test_string}'")
            print("No duplicate characters found.")
        else:
            print(f"Input: '{test_string}'")
            unique_repeats = sorted(set(result)) # Ensure strict uniqueness even if logic above has redundant checks (safety)
            output_str = ', '.join(unique_repeats)
            print(f"Duplicates: {output_str}")

    # Additional specific case to demonstrate functionality clearly with letters only for readability preference in examples
    # though the class handles all chars.
    test_letters = "banana"
    result_letters = analyzer.check_for_duplicates(test_letters)
    
    if not result_letters:
        print(f"\nInput (letters): '{test_letters}'")
        print("No duplicate characters found.")
    else:
        unique_repeats_letters = sorted(set(result_letters)) # Safety check for uniqueness again just in case logic drifts
        output_str_letters = ', '.join(unique_repeats_letters)
        print(f"Duplicates (letters): {output_str_letters}")