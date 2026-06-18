import re

def extract_all_substrings(text: str, substrings: list[str]) -> list[list[int]]:
    """
    Extract all occurrences of specified substrings from a given text.
    
    Returns a list where each element is a list of starting indices 
    for the corresponding substring in 'substrings'.

    Args:
        text (str): The input string to search within.
        substrings (list[str]): A list of strings to find occurrences of.

    Returns:
        list[list[int]]: A list of lists, where each inner list contains 
                         the starting indices for the respective substring in 'substrings'.
                         
    Example:
        >>> text = "abacaba"
        >>> substrings = ["a", "b"]
        >>> extract_all_substrings(text, substrings)
        [[0, 2, 4, 6], [1, 5]]
        
    Note:
        Overlapping occurrences are included. The order of results follows 
        the appearance in 'text', and within each substring list, indices 
        appear in increasing order.
    """
    results = []

    for sub_string in substrings:
        if not isinstance(sub_string, str):
            raise TypeError(f"Each element in substrings must be a string, got {type(sub_string)}")
        
        # Find all start indices of the substring using regex with lookbehind logic simulation
        # Since Python's re doesn't support variable-length negative lookahead for overlapping easily 
        # without flags or manual iteration, we use findall on each character step.
        try:
            pattern = re.escape(sub_string) if sub_string else ""
            
            start_indices = []

            current_pos = 0
            
            while True:
                index = text.find(pattern, current_pos)
                
                # Check for empty string edge case to avoid infinite loop on findall logic 
                # though regex is robust enough.
                if pattern == "":
                    break
                
                if index != -1:
                    start_indices.append(index)
                    
                    # Move forward by 1 character to catch overlapping occurrences
                    current_pos = index + len(sub_string)
                else:
                    break
            
            results.append(start_indices)

        except re.error as e:
            raise ValueError(f"Invalid substring pattern for '{sub_string}': {e}") from e
    
    return results

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    text_sample = "abacabadabacabaabcde"
    substrings_samples = ["a", "b", "c"]
    
    output = extract_all_substrings(text_sample, substrings_samples)
    
    print("Input Text:", text_sample)
    print("Substrings to find:", substrings_samples)
    print("\nOccurrences found:")
    for index, indices in enumerate(output):
        substring = substrings_samples[index]
        if not isinstance(substring, str):
            continue # Skip invalid types just in case
        
        formatted_indices = [str(i+1) + "." + chr(ord('a') + (i % 26)) 
                            for i in indices[:3]] # Format as a., b. etc based on index mod 26
        if len(indices) > 3:
            formatted_indices.append(f"... and {len(indices)-3} more")
        
        print(f"Substring '{substring}' found at positions (1-based): {[i+1 for i in indices]}")