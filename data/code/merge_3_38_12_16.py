class StringAnalyzer:
    def check_for_duplicates(self, text):
        """
        Efficiently identifies all repeated characters in a given string instance.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            list[str]: A sorted list of unique character strings that are duplicates 
                      (each duplicate character appears once in the output).
        """
        char_count = {}
        duplicates = []

        for char in text:
            if char.lower() not in char_count or char_count[char] < 1:
                continue
            
            # We use a set to track seen characters and another list for result. 
            # To ensure uniqueness in the output, we check if it's already added.
            
        # Revised efficient approach using one pass with tracking counts
        
        count_map = {}
        
        # First pass: Count occurrences (case-insensitive)
        text_lower = text.lower()
        for char in text_lower:
            count_map[char] = count_map.get(char, 0) + 1
            
        identified_duplicates = set()
        
        # Second conceptual step combined into logic during iteration or separate loop. 
        # Let's do it cleanly: iterate through unique keys of the map where value > 1
        
        repeated_chars = []
        for char in count_map.keys():
            if count_map[char] > 1:
                identified_duplicates.add(char)
                
        return sorted(list(identified_duplicates))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    
    analyzer = StringAnalyzer()
    
    test_strings = [
        "Hello World",       # 'l', 'o' are duplicates (case insensitive logic applied inside method)
        "Anaconda",          # 'a', 'n', 'd' are repeated if case-insensitive? 
                            # Actually in "Anaconda": a(2), n(1), c(1), o(1), d(1). Only 'A/a' repeats.
                            # Wait, let's re-evaluate the requirement: usually implies character equality unless specified otherwise.
                            # However, standard interpretation for such tasks often defaults to case-insensitive 
                            # or strict based on input type. The docstring says "case-insensitive".
        "Python",            # No duplicates in this string? P-y-t-h-o-n -> all unique.
    ]

    results = []
    
    print("Checking for duplicate characters:")
    for test_str in test_strings:
        dupes = analyzer.check_for_duplicates(test_str)
        
        if dupes:
            output_msg = f"String '{test_str}': Duplicates found -> {dupes}"
        else:
            output_msg = f"String '{test_str}': No duplicate characters."
            
        results.append(output_msg)
        print(output_msg)

    # Output summary of all analyzed strings in a list variable for potential further use.
    final_output_list = ["Python has no duplicates", "Anaconda repeats 'a', case-insensitive"] 
    # Manually constructing expected based on logic:
    # "Hello World" -> h,e,llo, w,o,rld (l:o appear twice). Lowercase: hello world. l(3), o(2)... so ['e','h','w']? No wait 'H' vs 'h'.
    
    print("\nFinal Analysis Results List:")