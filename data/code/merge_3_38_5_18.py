import collections

def find_duplicate_characters(s: str) -> list[str]:
    """
    Find all duplicate characters in a string using a hash map approach.
    
    This function iterates through the input string once, counting occurrences 
    of each character. It then collects only those characters that appear more than once.

    Time Complexity: O(n), where n is the length of the string (one pass for counting + one pass to check counts).
    Space Complexity: O(1) in terms of alphabet size (assuming fixed set of possible characters like ASCII/Unicode letters), 
                         or technically O(k) where k is the number of unique characters.

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A list containing all duplicate characters found in the string.
                   Order may vary based on insertion order preservation from Python 3.7+.
    
    Example:
        >>> find_duplicate_characters("aabbcc")
        ['a', 'b', 'c'] (order might differ depending on unique char encounter)
    """
    if not s:
        return []

    # Count frequency of each character in a single pass O(n)
    char_counts = collections.Counter(s)

    duplicates = [char for char, count in char_counts.items() if count > 1]

    return duplicates

if __name__ == '__main__':
    sample_string = "hello world! hello"
    
    # Hard-coded test case as per instructions (no user input required)
    result = find_duplicate_characters(sample_string)

    print(f"Duplicates found in '{sample_string}':")
    if not result:
        print("No duplicates.")
    else:
        for dup_char in set(result):  # Convert to set then back to str just to show unique chars nicely, but order from list is fine too.
            count = sample_string.count(dup_char)
            print(f"'{dup_char}': {count} occurrences")