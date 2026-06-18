def find_duplicate_characters(s: str) -> list[str]:
    """
    Find all duplicate characters in a string using O(n) time complexity.
    
    Args:
        s (str): Input string to search for duplicates
        
    Returns:
        list[str]: List of unique characters that appear more than once, sorted by appearance order

    Algorithm Explanation:
    - Use an array/list where the index represents ASCII value and another set 
      tracks which indices we've seen before. This gives O(n) time because 
      string indexing is constant on average in Python for single char lookups/assignments.
    """
    # Dictionary to track character counts (more explicit than raw list of size 128+)
    from collections import Counter
    
    count = Counter(s)
    
    # Find characters with count > 1, maintaining order based on first appearance
    result = []
    seen_indices = set()  # Track indices where we've added a duplicate to avoid re-addition

    for idx, char in enumerate(s):
        if count[char] > 1 and char not in seen_indices:
            result.append(char)
            seen_indices.add(idx)
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values - no user input required
    test_cases = [
        "hello",           # Expected: ['l', 'o']
        "programming",     # Expected: ['g', 'r', 'm']
        "aabbccdd",        # Expected: ['a', 'b', 'c', 'd']
        "no-duplicates",   # Expected: [] (assuming only one occurrence of hyphen)
    ]

    for test_string in test_cases:
        duplicates = find_duplicate_characters(test_string)
        print(f"Input: '{test_string}'")
        if not duplicates:
            print("No duplicate characters found.")
        else:
            # Format output to show only unique duplicated chars in order of appearance
            sorted_duplicates = list(dict.fromkeys(duplicates))  # Re-addition guard just in case logic changes slightly, though we already handled it. 
            # Actually our main loop ensures uniqueness per string iteration based on first occurrence index.
            print(f"Duplicate characters: {sorted_duplicates}")
        print("-" * 40)