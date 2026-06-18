def yield_concatenated_segments(strings_iterable: Iterable[str], separator: str = "") -> Generator[str, None, None]:
    """
    Yields concatenated string segments from an iterable of strings using a custom separator.
    
    This function takes an iterable of strings and yields them as single concatenated 
    result with the specified separator inserted between each segment if provided.
    If no separator is given or it's empty, all non-empty consecutive segments are joined directly.
    
    Args:
        strings_iterable (Iterable[str]): An iterable containing string elements to be processed.
        separator (str): A custom separator string to insert between concatenated parts. Defaults to "".

    Yields:
        str: The resulting concatenated string segment(s). If the input list contains multiple 
             non-empty segments, they are joined with the separator; otherwise, if only one or empty elements exist, 
             it yields a single combined result (or an empty string if all inputs are effectively skipped/empty in context of joining logic that skips empties unless specified otherwise - here we join everything including potential internal separators).
             
    Note: This implementation joins ALL strings from the iterable into a single segment with the separator between them. 
          If you intended to split by some criteria first, additional filtering or grouping would be needed outside this function's scope as per standard concatenation behavior unless specified otherwise in complex scenarios not covered here for simplicity and generality without over-engineering based on "concatenated string segments" phrasing which typically implies joining parts together.
    """
    
    # Convert iterable to list for processing, though generator works too if we iterate once internally
    items = list(strings_iterable)
    
    # Filter out empty strings or handle them? The prompt says "segments", implying meaningful chunks. 
    # However, standard concatenation usually includes all unless told otherwise. Let's assume include all but join with separator.
    # Re-reading: "concatenated string segments" could mean if input is ["a", "", "b"], output should be "ab" or "a b"? 
    # Given custom separator usage, likely intended to separate non-empty meaningful parts OR just join everything.
    # To make it robust and useful as a generator for segmenting: we'll collect all strings and join them with the separator regardless of emptiness? 
    # Actually, if input is ["x", "y"], output should be one string "xy" or "x+y"? With custom sep="+", then "x+y".
    # If multiple segments are expected per call (like splitting by a delimiter inside?), that's different. But the task says from an iterable of strings -> yields concatenated ones. 
    # Likely: take all input, join them with separator into one big string and yield it once? Or if there are groups? 
    # Since no grouping logic is specified, we assume flat concatenation of all items in order using the separator between each adjacent pair.
    
    result_parts = []
    for item in items:
        result_parts.append(item)
        
    joined_string = "".join(result_parts).replace("", "") if not separator else "" # placeholder
    
    # Correct approach: join with separator
    final_result = sep.join(result_parts)

    yield final_result

def main():
    """
    Main execution block to demonstrate the generator function.
    Uses hard-coded sample values as per requirements (no user input, args, etc.).
    """
    
    # Sample data: list of strings to concatenate with a custom separator
    sample_strings = ["Hello", "World", "!"]
    custom_separator = "-"

    print("Generating concatenated segments...")
    for segment in yield_concatenated_segments(sample_strings, custom_separator):
        print(segment)

if __name__ == '__main__':
    main()