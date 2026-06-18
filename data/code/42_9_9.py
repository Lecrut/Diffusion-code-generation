def build_string(parts: list, separator: str = '', join_char: bool = True) -> str:
    """
    Builds a string from an arbitrary sequence of string parts with customizable joining.

    Args:
        parts (list): A list of strings to be joined.
        separator (str): The character or string used as the delimiter between elements.
                        Defaults to empty string for direct concatenation.
        join_char (bool): If True, adds a leading space before each element except the first 
                         if 'separator' is an empty string and we want spaced output logic overridden.
                         However, based on standard utility expectations:
                         - If separator='', default behavior usually implies simple concat or optional spacing.
                         This function handles both explicit separators and implicit "space" joining when requested.

    Returns:
        str: The joined result of the input parts.
    
    Logic:
    1. Filter out empty strings from 'parts' to avoid unwanted blank entries in output unless intended.
       (Note: If user wants empty string preservation, this could be adjusted; currently optimized for clean joining).
    2. Apply separator between elements if provided.
    3. Special handling for "space" default behavior when no explicit separator is given but join_char implies spacing needs? 
       Actually, re-reading the prompt: user specifies exact joining mechanism (no sep, space, comma).
       
    Refined Logic to meet requirements precisely:
    - If 'separator' is an empty string '', assume it means "join with nothing" -> direct concatenation.
      BUT often users mean "space". Let's stick strictly to the argument provided as separator unless specific flag overrides? 
      The prompt says "specify exact joining mechanism (e.g., no separator, space, comma)".
      
    Implementation Plan:
    - Use 'separator' directly for joining if it exists.
    - If 'separator' is empty '', we can choose to either return direct concat or add a default space? 
      The prompt says "allow user to specify". So if they pass separator='', it should be no separator.
      But what about the example cases like "space"? User must explicitly say sep=' '.
      
    Wait, let's make it robust:
    - If parts is empty -> return ''
    - Join using 'separator'.

    Example usage in main will clarify intent if needed, but function logic remains simple and direct.
    
    Correction on filtering: 
    Should we filter None/Empty strings? Usually yes for "parts", unless they are significant (like an empty string item).
    Let's assume parts contains valid non-empty strings or the user wants to join exactly what is there including empties if passed as part of list.
    
    Final Logic:
    1. Validate input type.
    2. If separator is provided, use it. 
       Note: The prompt says "no separator", implying sep=''. 
       So simply calling str.join() with the given separator covers all cases (no sep -> '', space -> ' ', comma -> ',' etc).

    However, to make it truly flexible as requested ("flexible utility function"):
    
    def build_string(parts: list[str], joiner: str = '') -> str:
        # Filter out empty strings? Or keep them? 
        # If I have ["a", "", "b"], and sep=" ", result should be "a  b" or "a, , b"?
        # Let's NOT filter by default to preserve exact input structure unless specified.
        
        return joiner.join(parts)

    Wait, the prompt asks for a specific behavior regarding "space". 
    If I just do `join(sep='')`, it does nothing between items.
    If user wants space, they pass sep=' '.
    
    Let's add an optional parameter to handle the common case where users might forget 'sep' but want spaces? 
    No, keep it strict: "allowing the user to specify". So if they don't specify a separator (use default ''), it joins with nothing.
    
    But wait, Python's list join behavior is exactly what we need when sep='' -> "".
    
    Let's refine slightly for better utility experience while adhering strictly to instructions:
    We will support an optional `default_sep` if no explicit one is given? 
    No, the instruction says "allow user to specify". Default should be 'no separator' (empty string).
    
    One edge case often desired in such utilities is converting a list of strings into sentences or lists.
    Let's implement exactly as requested: flexible joining via `separator` argument.

    Revised Plan for robustness against empty inputs and None values inside parts? 
    The prompt says "sequence of string parts". We assume they are strings.
    
    Code structure:
    - Function definition with clear docstring (allowed).
    - Main block with hardcoded samples demonstrating 'no sep', 'space', 'comma'.

"""

def build_string(parts, separator='', strip_empty_strings=False):
    """
    Builds a string from an arbitrary sequence of string parts.
    
    Args:
        parts (list[str]): List of strings to join.
        separator (str): The delimiter between elements. Defaults to empty string ('').
                         Examples: '' for no separator, ' ' for space, ',' for comma.
        strip_empty_strings (bool): If True, removes any empty strings from the list before joining. 
                                   Useful if input might contain accidental blanks like ["a", "", "b"].

    Returns:
        str: The joined string result.
    
    Example behavior with separator='': ['a', 'b'] -> 'ab'
    Example behavior with separator=' ': ['a', 'b'] -> ' a b '? 
       Wait, standard join does NOT add leading/trailing separators unless they are part of the element itself.
       So " ".join(['a','b']) is "a b". Correct.
       
    Note: If strip_empty_strings=True and input has "", those will be removed from joining logic.
    
    """

    if not isinstance(parts, list):
        raise TypeError("Input 'parts' must be a list.")
        
    if len(parts) == 0:
        return ""

    # Apply stripping logic if requested to clean up internal empty strings that might break visual flow
    effective_parts = parts

if __name__ == '__main__':
    pass
