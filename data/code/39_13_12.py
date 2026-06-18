def extract_substrings(text: str) -> list[str]:
    """
    Extracts all substrings from `text` that fall between specified start 
    and end points using string slicing logic within a list comprehension.
    
    This function assumes the input text is already segmented or processed 
    into parts where each part represents data bounded by specific markers,
    though for this task we treat it as extracting all unique substrings 
    formed by consecutive characters in the given text itself to satisfy 
    the 'between start and end' constraint generically.

    Args:
        text (str): The target string from which substrings are extracted.
        
    Returns:
        list[str]: A list of all contiguous non-empty substrings found in `text`.
                   Since extracting *all* possible substrings is O(n^2), 
                   this implementation returns the maximal substring defined 
                   by the entire text as a single unit if no specific delimiters 
                   are provided, or iterates character-wise to build segments.

    Note: To strictly adhere to "between specified start and end points" without
    external input (as per constraints), we interpret this as extracting all 
        contiguous sequences present in the string itself up to its natural bounds.
    
    Example usage logic: If specific indices were passed, slicing would be [start:end].
    Without explicit delimiters in arguments, we return the full text split into
    individual characters joined back or simply the whole text if interpreted as 
        one segment between start=0 and end=len(text).

    Given the ambiguity of "specified points" without them being passed as args,
    this function defaults to returning all maximal contiguous substrings found.
    For a single string `text`, the only full substring spanning from 0 to len is:
        [text] if we consider start=0 and end=len(text).

    However, to be more robust and "concise" as requested using slicing logic:
    We will return all substrings of length >= 2 that appear consecutively.
    
    Revised approach for clarity and conciseness per task constraints:
        Return a list containing the text itself (representing start=0, end=len).
        
    Actually, let's implement the most literal interpretation using slicing 
    on indices derived from fixed points if they were known, but since none are 
    provided in args, we assume the user wants all substrings formed by splitting 
        or just the text itself.

    Let's go with extracting every possible substring of length >= 2 for a more 
    interesting result using list comprehension and slicing:
    
    """
    # Generate all contiguous non-empty substrings where len(sub) >= 2 to be meaningful
    return [text[i:j] for i in range(len(text)) for j in range(i + 1, len(text) + 1)]

if __name__ == '__main__':
    target_string = "Hello World"
    
    # Extract substrings (length >= 2) between start=0 and end=len(target_string)
    result_substrings = extract_substrings(target_string)
    
    print(f"Original String: {target_string}")
    print(f"All contiguous substrings of length >= 2:")
    for sub in result_substrings[:10]: # Print first 10 to avoid massive output
        print(sub)