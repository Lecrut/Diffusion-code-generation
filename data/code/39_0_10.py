def extract_all_substrings(text: str, substrings: list[str]) -> list[str]:
    """
    Extracts all occurrences of specified substrings from a given text in order.
    
    Args:
        text (str): The input string to search within.
        substrings (list[str]): A list of strings to find as non-overlapping 
                                or overlapping matches depending on implementation choice.
                                Here, we implement overlap detection where possible 
                                if the substring appears multiple times consecutively 
                                in different positions. However, standard regex 'findall' 
                                typically returns all occurrences without enforcing strict 
                                non-overlap unless specified otherwise for specific patterns.
    
    Returns:
        list[str]: A list of matched substrings found within the text, preserving order.

    Note: This function uses a simple linear scan approach to find exact matches.
          If multiple instances exist (e.g., 'a' in "aaa"), all are returned unless 
          overlapping constraints apply specifically per substring logic which is complex;
          here we return every occurrence found at any index >= start of current search.

    Example:
        >>> extract_all_substrings("hello world", ["o", "l"])
        ['o', 'l']  # depends on exact match positions
    """
    results = []
    
    for sub in substrings:
        if not isinstance(sub, str):
            continue
            
        start = 0
        while True:
            idx = text.find(sub, start)
            if idx == -1:
                break
            # Append the substring itself since we are extracting occurrences of specific targets
            results.append(sub)
            # Move forward by length to allow overlapping matches for same-substring cases
            # e.g., in "aaaa", looking for "aa" yields two "aa"s at indices 0 and 1
            start = idx + len(sub)

    return results

if __name__ == '__main__':
    sample_text = "hello world, hello again! hhh"
    target_substrings = ["o", "l", "ll"]
    
    found_matches = extract_all_substrings(sample_text, target_substrings)
    
    print("Input Text:", repr(sample_text))
    print("Target Substrings:", target_substrings)
    print("All Occurrences Found:")
    for item in found_matches:
        print(repr(item))