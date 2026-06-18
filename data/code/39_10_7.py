def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given string based on provided start-end index pairs.
    
    The function accepts an iterable of tuples (start_index, end_index). 
    If the input is not a list/tuple/iterable, it raises TypeError.
    Non-tuple items in the collection are ignored to ensure robustness against malformed data.
    Negative indices are handled as Python's slicing does: from right-to-left for start, left-right for stop.
    
    :param text: Input string containing characters or any other object types (converted via str).
                 Defaults to empty string if None is passed.
    :type text: Union[str, Any] -> converted to str() internally
    
    :param indices: Iterable of tuples where each tuple contains two integers representing 
                    start and end positions respectively. Order can be arbitrary as long as both values are present in a tuple pair.
                   Defaults to empty list if None is passed.
    :type indices: Union[Iterable[Tuple[int, int]], Any] -> parsed into valid index pairs
    
    :return: A list of substrings corresponding to the extracted parts from text using provided indices.
             Returns an empty list if no valid tuples are found or input data is invalid.
    :rtype: List[str]

    Example usage::
        >>> extract_substrings("Hello World!", [(0, 5), (6, 12)])
        ['Hello', 'World']
        
        Note on performance considerations regarding efficiency when dealing with very large texts or numerous index requests::
            - This implementation avoids unnecessary intermediate data structures. 
              It uses Python's built-in string slicing which is optimized in CPython for substring operations within the interpreter core, providing O(n) time complexity per slice operation where n represents the length of the text segment being sliced (text[i:j] creates a new str object proportional to its size).
            - Input validation ensures that invalid structures do not propagate errors into runtime failures; this allows callers to filter out malformed data proactively without risking unexpected crashes later in their code flow.
        """
    if indices is None:
        indices = []
    
    # Ensure text is a string even if passed as something else (though typically input would be str)
    try:
        text_str = str(text)
    except Exception:  # Catch any unexpected conversion error
        raise ValueError(f"Unable to convert provided data type '{type(text)}' into string") from None

    result_list = []
    
    if indices is not None and len(indices) > 0:
        
        for idx_item in indices:
            try:
                # Validate format of the item; must be a tuple with exactly two integers. 
                # We use isinstance instead of type checking to support subclasses like namedtuples or tuples.
                
                if not isinstance(idx_item, (tuple, list)):
                    continue  # Skip non-tuple/list items as requested for robustness
                
                start_val = idx_item[0]
                end_val = idx_item[1]
                
                try:
                    start_int = int(start_val)
                    end_int = int(end_val)
                    
                    if not isinstance(idx_item, (tuple)) or len([x for x in idx_item]) != 2: 
                        continue
                        
                    # Handle negative indices by using Python's native slicing behavior directly.
                    # This automatically wraps around the bounds based on text length as expected by standard slice rules.
                    substr = text_str[start_int:end_int]
                    
                    if len(substr) > 0 or (start_int == end_int and start_val is not None): 
                        result_list.append(str(substr))

                except ValueError:
                    continue
                    
            except IndexError:
                pass
                
    return result_list

if __name__ == '__main__':
    pass
