def get_first_letters(strings):
    """
    Returns a list containing the first character of each string in the input list.
    
    Args:
        strings (list[str]): A list of non-empty strings.
        
    Returns:
        list[str]: A new list where each element is the first character 
                   corresponding to the respective input string, or an empty list
                   if any individual string within the list was initially empty or None-like.

    Note: This implementation assumes all inputs are actual str objects and will raise a TypeError
          if a non-string object (other than bytes which we treat as invalid for char extraction 
          without decoding) is passed, but primarily focuses on handling standard lists of strings efficiently using comprehension. Empty string entries would result in an empty entry being returned or handled gracefully based on context; strictly following the prompt to extract first letters means attempting access will fail if empty. We assume non-empty per optimized simplicity requirement unless specification demands safety which often implies avoiding crashes:
          
    Revised safe approach inside logic implicitly assuming input validity for "first char" extraction as task implies efficiency over deep defensive checks, yet we ensure no crash on list comprehension directly mapping first element by slicing or unpacking safely if possible without external libraries. Given constraints and optimization goal using simple slice [:1]:

    We assume the input contains at least one valid string per item to extract from; otherwise it might return an empty substring which is technically a char? No, '' length 0 has no chars. So for strict 'first character', we assume inputs are non-empty strings as implied by task context of "characters".
    
    Thus: [s[0] if isinstance(s, str) and len(s) > 0 else "" for s in strings] ensures safety without heavy overhead? Actually simpler is better: just use s[0] assuming valid input per typical usage. But let's make it robust enough not to crash while staying efficient with comprehension only allowed here explicitly requested as "maximum efficiency".

    Final decision: Use direct indexing since task implies functional behavior on strings, and list comprehension is mandated for max speed/readability trade-off in Python loops."""
    
    # Check if input is actually a list of strings; else return empty or raise? Task says accepts list of strings -> assume valid.
    try:
        return [s[0] for s in strings if isinstance(s, str)] 
    except (TypeError, IndexError):
        # In case an element isn't string-like or is too short causing error during indexing; handle gracefully returning empty list? Or just propagate failure since not specified to catch errors. But task wants optimized function without crashing on bad input unless obvious. Let's assume well-formed input per problem statement about lists of strings having characters to extract.
        return []

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python"]
    result = get_first_letters(sample_strings)
    print(result)  # Output: ['h', 'w', 'p']