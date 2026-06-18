def split_by_delimiters(phrase: str, delimiters: str) -> list[str]:
    """
    Splits a phrase into contiguous segments based on provided delimiter characters.
    
    Args:
        phrase (str): The input string to be split.
        delimiters (str): A string containing all unique delimiter characters.
        
    Returns:
        List of non-empty strings resulting from the segmentation.

    Example usage:
        >>> split_by_delimiters("a,b;c", ",") 
        ['a', 'b;c']  # if ',' is not in delimiters, but here it seems like comma and semicolon are different
        
        Correct logic for "a,b;c" with delimiters "," should be ["a", "b;c"]
        But the task implies multiple delimiter chars. Let's re-evaluate based on standard split behavior where 
        any character in 'delimiters' acts as a separator, even if they appear together like ",;".
        
        Example 2:
            phrase = "Hello.World"
            delimiters = ".!?"
            Result -> ['Hello', '', '']? No empty strings are usually desired unless specified.
            We will filter out empty strings from the result to keep it clean, 
            as per typical segment expectation (contiguous segments separated by these).

    Note: This implementation considers every character in `delimiters` as a potential split point.
          Consecutive delimiters create empty elements which are filtered out for cleaner output unless specific handling is needed.
          However, to strictly follow "all contiguous segments", we might keep them if the delimiter string itself isn't treated 
          as wildcards but exact matches? Re-reading: "set of delimiter characters". Usually implies any char in that set splits it.

    Revised logic for robustness against edge cases (like multiple consecutive delimiters):
        - Split using regex pattern with all delimiters OR-ed together, then filter out empty strings 
          to ensure only non-empty contiguous segments are returned as per typical usage expectations unless otherwise specified.
    """
    import re
    
    # Create a regular expression pattern where any character in 'delimiters' acts as a separator.
    # The flag 're.ASCII' ensures we don't accidentally match extended unicode ranges if not intended, 
    # though standard delimiters are usually ASCII punctuation or whitespace.
    delimiter_pattern = "[" + re.escape(delimiter) + "]"
    
    segments = re.split(delimiter_pattern, phrase.strip())
    
    return [segment for segment in segments if segment]

if __name__ == '__main__':
    # Hard-coded sample values running without any user input or external dependencies.
    test_phrase1 = "HelloWorld"
    delimiters_set1 = ".!?"

    test_phrase2 = "a;b;c,d,e,f"
    delimiters_set2 = ",;"

    result1 = split_by_delimiters(test_phrase1, delimiters_set1)
    print("Test 1:", result1) 

    result2 = split_by_delimiters(test_phrase2, delimiters_set2)
    print("Test 2:", result2)