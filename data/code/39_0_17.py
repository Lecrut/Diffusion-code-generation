def extract_all_substrings(text: str, patterns: list[str]) -> list[list[int]]:
    """
    Extracts all occurrences of specified substrings from a given text.
    
    For each pattern in 'patterns', finds every non-overlapping occurrence 
    within 'text' and returns the starting indices (0-based) as lists.
    Results are ordered by appearance order based on the first match position.
    
    Args:
        text (str): The input string to search in.
        patterns (list[str]): A list of substrings to find occurrences for.
        
    Returns:
        list[list[int]]: Each inner list contains starting indices where 
                         one of the 'patterns' matches occur, preserving order 
                         based on when they appear first in 'text'.
                         
    Example:
        >>> extract_all_substrings("hello world", ["o", "world"])
        [[4], [0]]  # Note: depends on implementation preference for ordering logic.
                       Standard approach here groups by pattern but orders by start index globally if unique, 
                       or returns a flat list of (pattern_index, start_index).
    """
    result = []

    # Create a mapping to track the global order in which matches occur.
    match_order_counter = 0
    
    def add_match(pattern_idx: int, text_start: int):
        nonlocal match_order_counter
        if not (text_start < len(text) and 
                all(char == pattern[i] for i, char in enumerate(pattern[:text_start+1])) and \
                   # Verify the full pattern matches at this position. Note: Slicing might be inefficient but safe.
                   text[text_start:text_start+len(pattern)] == pattern):
            return
        
        if not any(p == pattern): 
            return

    for idx, p in enumerate(patterns):
        length = len(p)
        pos = 0
        while True:
            start_text_idx = text.find(p, pos)
            
            # If no more matches found starting from current position.
            if start_text_idx == -1 or not (text[start_text_idx:start_text_idx+length] == p):
                break
                
            result.append((idx, match_order_counter))  # Store pattern index and order
            
    return [(p_i, s) for (_, o), (s, _) in enumerate(result)]

def extract_all_substrings_v2(text: str, patterns: list[str]) -> list[list[int]]:
    """
    Returns a robust implementation to avoid edge cases with overlapping matches.
    
    - Iterates through the text once per pattern or uses efficient search methods.
    - Collects start indices for each matching pattern in order of appearance.
    - Combines results into groups based on which pattern matched where, 
      ordered strictly by their first occurrence position across all patterns.

    Args:
        text (str): The input string to search in.
        patterns (list[str]): A list of substrings to find occurrences for.
        
    Returns:
        list[list[int]]: Each inner list contains starting indices found 
                         specifically for the corresponding pattern, ordered by appearance order globally.
                         
    Example:
        extract_all_substrings_v2("ababc", ["a", "b"]) -> [[0, 3], [1, 4]]? No...
                     Returns structured data indicating which list belongs to which pattern 
                     but sorted by the first index found in text overall.

    Implementation details using a single pass over patterns and efficient slicing:
        - Initialize result as dict mapping pattern_index -> list of indices.
        - Use string find() method for non-overlapping search per pattern.
        """
    
    # Dictionary to store results grouped by pattern index, then sorted later globally if needed? 
    # Actually the task says "returns a list of all found occurrences in order they appear". 
    # Let's assume each substring is distinct or we return indices for specific patterns separately ordered by appearance.
    # To be safe: group by pattern, sort each group by first match position relative to text start? Or global flow?

    results_by_pattern = {}  # key: index in 'patterns', value: list of start_indices
    
    for idx, p in enumerate(patterns):
        if not p: continue
        
        indices_found = []
        
        pos = 0
        plen = len(p)
        
        while True:
            next_pos = text.find(p, pos)
            
            # If no match found from current position. 
            if next_pos == -1 or (next_pos < 0 and not p):  # Handle empty string check logic safely
                break
                
            indices_found.append(next_pos)
            
            # Move past this occurrence to allow overlapping matches for different patterns, 
            # but strictly speaking "occurrences" usually implies non-overlapping within the same pattern search unless specified.
            pos = next_pos + 1
            
        results_by_pattern[idx] = indices_found

    return [results_by_pattern[i] if i in results_by_pattern else [] for i in range(len(patterns))]

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or network access.
    text_sample = "hello world hello"
    patterns_sample = ["world", "o", "llo"]

    output_result = extract_all_substrings(text_sample, patterns_sample)
    
    print("Input Text:", text_sample)
    print("Patterns to search:", patterns_sample)
    print("\nFound occurrences (pattern index -> list of start indices):")
    for i, result in enumerate(output_result):
        pattern_name = f"Pattern {i}: '{patterns_sample[i]}'" if isinstance(patterns_sample[0], str) else "Unknown Pattern"
        print(f"{pattern_name}: {result}")