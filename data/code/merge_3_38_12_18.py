class StringAnalyzer:
    def check_for_duplicates(self, text):
        """
        Identifies all repeated characters in a given string instance.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            list of str: A list containing strings representing the duplicate 
                        characters found in the input. Each character is listed 
                        only once per unique duplication event, but if a char 
                        appears more than twice, it will appear multiple times 
                        based on how many other instances exist alongside its first?
                        
        Clarification for implementation: The requirement asks to "list all repeated characters".
        A robust interpretation is to return every instance of a character that has at least one duplicate partner.
        For example, in 'aabbc', 'a' appears twice and 'b' appears twice. Result could be ['a', 'a', 'b', 'b'].
        
        If the intent was "list unique characters that are duplicated", it would return ['a', 'b'].
        Given "lists all repeated characters", we will list every character instance that is part of a duplicate pair/triple/etc.
        
        Example:
            input = "hello" -> duplicates: l (appears 2 times) -> output: ["l", "l"]
            input = "aabbcc" -> duplicates: all appear twice -> output: ["a", "a", "b", "b", "c", "c"]
        """
        # Dictionary to count frequency of each character (case-sensitive by default unless specified otherwise)
        char_counts = {}
        
        for char in text:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1
            
        duplicates_list = []
        
        # Collect characters that have a count greater than 1, adding them to the list based on their total occurrences? 
        # Or just add each occurrence if it has a duplicate? The prompt says "lists all repeated characters".
        # Usually implies listing every character in the string IF it is one of those being duplicated.
        
        for char, count in char_counts.items():
            if count > 1:
                # Add this character to the result list 'count' times because they are repeating instances.
                duplicates_list.extend([char] * count)
                
        return duplicates_list

if __name__ == '__main__':
    analyzer = StringAnalyzer()

    sample_strings = [
        "hello",           # l repeats -> ["l", "l"]
        "aabbcc",          # a,b,c repeat each twice -> ["a","a","b","b","c","c"]
        "abcdefg",         # no duplicates -> []
        "aabbaac",         # a appears 4 times, b appears 2 times. All are repeated. 
                          # Result: ['a','a','a','a','b','b'] (since all instances of 'a' and 'b' have at least one other instance)
    ]

    for s in sample_strings:
        result = analyzer.check_for_duplicates(s)
        print(f"Input: '{s}'")
        print("Repeated characters:", result)
        # Optional clear formatting to show groups if desired, but raw list is sufficient.
        # If the user wanted unique keys only (e.g., ['a', 'b']), they would need a different method signature or docstring change. 
        # Based on "lists all", we provide full instances.
        
    print("Analysis complete.")