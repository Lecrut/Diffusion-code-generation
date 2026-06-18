import re

def find_substring_matches(text: str, patterns: list[str]) -> dict[str, list[str]]:
    """
    Takes a string and a list of regex patterns.
    Returns a dictionary where keys are the pattern strings (as written) 
    and values are lists of all non-overlapping substrings in 'text' that match each pattern.

    Args:
        text (str): The input string to search within.
        patterns (list[str]): A list of regex pattern strings.

    Returns:
        dict[str, list[str]]: Mapping from pattern to its matching substrings found in the text.
    
    Note: 
    - Matches are non-overlapping for each specific pattern scan.
    - The order of matches within a list follows their appearance in 'text'.
    """
    results = {}

    # Compile all patterns first for efficiency, though we keep original strings as keys
    compiled_patterns = []
    
    for p_str in patterns:
        try:
            compiled_pattern = re.compile(p_str)
            compiled_patterns.append((p_str, compiled_pattern))
        except re.error as e:
            # In case of invalid regex pattern, store an empty list to indicate failure or skip? 
            # The task implies valid inputs usually. We'll include it with an error message logic if needed, 
            # but strictly returning matches suggests we assume valid patterns unless specified otherwise.
            # Let's handle gracefully by putting None in the list for that pattern key.
            results[p_str] = [None] 

    for p_str, compiled_pattern in compiled_patterns:
        found_matches = []
        
        if not text or len(text) == 0:
            continue
            
        start_index = 0
        
        while True:
            match = compiled_pattern.search(text, pos=start_index)
            
            # If no more matches are found from this position onwards
            if not match:
                break
                
            matched_text = match.group()
            found_matches.append(matched_text)
            
            # Move start index to the end of the current match to ensure non-overlapping behavior 
            # for a single pattern scan. If overlapping was required, we would increment by 1 instead.
            start_index = match.end()

        results[p_str] = found_matches
        
    return results

if __name__ == '__main__':
    sample_text = "abracadabra"
    
    # Sample patterns: 
    # 'a' -> matches all 'a's
    # '[bc]' -> matches 'b', 'c' (case sensitive)
    # '^.*d.*$' -> This is a regex that might match the whole string if anchored correctly, but here it acts as substring search logic. 
    # However, re.search on ^.*d.*$ inside "abracadabra" will find matches starting from index 0 up to 'd', then continue?
    # Actually, '^' anchors at start of string for the whole match in standard regex behavior unless flags are used differently.
    # But since we use search() which finds anywhere: 
    # Wait, ^.*d.*$ means "from start of line (or string) to 'd', then anything". In a single pass scan with non-overlapping logic:
    # It will find the first match starting at 0. The group is everything from index 0 until it hits end? No.
    # Let's stick to simple patterns for clarity in sample.
    
    pattern_list = [
        "a",           # Single character 'a'
        "[bc]",       # Character class matching b or c
        "^.*d.*$",   # This is tricky with search(). It matches from start of string up to first d? No, .* consumes greedily. 
                     # Actually ^ anchors at beginning. So it must match starting at 0. Then .* eats until 'd'. Then .* eats rest.
                     # But re.search returns the whole matched span. In "abracadabra", there is only one such substring: "abracadabra" itself? 
                     # Let's verify logic: ^ matches start. .* matches as much as possible (end of string). d must be found before end? No, greedy .* goes to end first.
                     # Backtracking will happen until 'd' is matched. So it finds the longest suffix ending in something that satisfies the pattern? 
                     # Actually: ^.*d.*$ on "abracadabra":
                     # 1. Try match from start. .* takes everything up to last char? No, d must be present. Greedy .* tries end of string first (fails). Backtracks until 'a' is before 'b', then 'c'? 
                     # Eventually it finds the sequence where ^ matches index 0, .* consumes "abra", then 'd' matches at index 5 ("acad..."). Then .* consumes "abra".
                     # So one match: "abracadabra".
    ]

    output = find_substring_matches(sample_text, pattern_list)

    print("Input Text:", sample_text)
    print("\nPattern Matches:")
    
    for p_str in sorted(output.keys()):
        matches = output[p_str]
        if None in matches:
            status = "ERROR"
        else:
            # Convert list of strings to a readable format, e.g., joined by comma or just printed as is. 
            # Since the requirement asks for 'list', printing it directly is fine but formatted looks better.
            print(f"\nPattern '{p_str}':")
            if not matches:
                print("  No matches found.")
            else:
                match_items = ", ".join(repr(m) for m in matches)
                print(f"  Matches: {match_items}")