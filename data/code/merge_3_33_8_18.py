def remove_internal_spaces(strings):
    """
    Returns a new list where every string in the input has its internal spaces removed.
    
    Args:
        strings (list of str): The list of strings to process.
        
    Returns:
        list of str: A new list with internal spaces stripped from each string.
                     Leading and trailing whitespace is preserved, only consecutive 
                     inner spaces are collapsed into a single space if present? 
                     Actually re-reading the task: "internal spaces removed".
                     This usually implies removing ALL spaces that are not part of intended formatting,
                     but often in such tasks it means collapsing multiple internal spaces to one.
                     
    However, looking at common interpretations for this specific phrasing without further context:
    1. Remove all space characters entirely? -> "hello world" becomes "helloworld"
    2. Collapse multiple consecutive spaces into one? -> "hello   world" becomes "hello world"
    
    Given the phrase "internal spaces removed", I will interpret this as removing ALL whitespace 
    characters from within the string, effectively joining all words together without any separators.
    If the intent was collapsing to single space, it would usually say "collapse multiple spaces".
    But wait, "removed" is strong. Let's look at edge cases like leading/trailing.
    
    Re-evaluating based on standard coding interview patterns for this specific wording:
    Often "remove internal spaces" means removing the space character itself wherever it appears 
    inside the string boundaries (i.e., not preserving any spacing).
    
    Example: ["a b", "c d e"] -> ["ab", "cde"]
    
    Let's implement removal of all space characters. If leading/trailing were meant to be kept,
    the prompt would likely specify "internal" in a way that distinguishes them from boundaries, 
    or say "collapse". Since it says "removed", I will remove every ' '. 
    
    Actually, let's reconsider standard behavior for such tasks. Usually, if someone wants 
    no spaces at all they say "remove all spaces". "Internal spaces removed" might imply keeping
    the first and last character logic? No, that doesn't make sense with lists of strings.
    
    Let's stick to the most literal interpretation: Remove every space character from inside the string.
    Since a list item is its own container, removing internal spaces means replacing ' ' with ''.
    
    Implementation detail: Use str.replace(' ', '') for each element."""
    return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    sample_list = ["hello world", "foo bar baz", "no spaces here", "  multiple   spaces  "]
    
    result = remove_internal_spaces(sample_list)
    
    print("Input:", sample_list)
    print("Output:", result)