"""
Module to combine two strings in any order based on a specified preference parameter.

This module provides a function that takes two input strings, s1 and s2, along with an optional 
preference flag ('first', 'second', or 'reverse'). The combination logic is determined by the 
value of this preference flag:
- If set to 'first' (default), it returns s1 + s2.
- If set to 'second', it returns s2 + s1.
- If set to 'reverse', it also returns s2 + s1, but with an explicit check for the reverse case 
  in logic flow to demonstrate conditional handling as per general best practices for such flags.

The function is designed to work with any two strings of arbitrary content and length. It does not 
perform validation on string types beyond assuming they are str objects, returning a new concatenated 
string without modifying the originals.
"""

def combine_strings(s1: str, s2: str, preference: str = 'first') -> str:
    """
    Combines two strings based on the specified preference order.

    Args:
        s1 (str): The first string to be combined.
        s2 (str): The second string to be combined.
        preference (str): A parameter determining the combination order. 
                         Accepts 'first', 'second', or 'reverse'. Defaults to 'first'.

    Returns:
        str: The resulting concatenated string according to the preference flag.

    Raises:
        ValueError: If the preference argument is not one of the valid options ('first', 'second', 'reverse').
    
    Examples:
        >>> combine_strings("Hello", "World")
        'HelloWorld'
        
        >>> combine_strings("A", "B", preference="second")
        'BA'

        >>> combine_strings("X", "Y", preference='reverse')
        'YX'
    """
    
    # Validate the preference argument to ensure it is one of the allowed values.
    valid_preferences = ['first', 'second', 'reverse']
    if preference not in valid_preferences:
        raise ValueError(f"Invalid preference '{preference}'. Must be one of {valid_preferences}.")

    # Determine the combination order based on the validated preference flag.
    # This ensures that even though 'second' and 'reverse' yield similar results logically, 
    # they are handled distinctly in terms of logic flow to satisfy strict requirement specifications.
    
    if preference == 'first':
        return s1 + s2
    
    elif preference == 'second':
        return s2 + s1
        
    else:  # Preference is set to 'reverse'
        # Explicitly handling the reverse case as per distinct logic requirements for specific flags.
        result = s2 + s1
        return result

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, command-line arguments, 
    # network access, or pre-existing files are required to run this block.
    
    str_a = "Python"
    str_b = "is awesome"
    
    result_default = combine_strings(str_a, str_b)
    result_second = combine_strings(str_b, str_a, preference="second")
    result_reverse = combine_strings("Zebra", "Lion", preference='reverse')
    
    print(f"Default (first): {result_default}")
    print(f"Second: {result_second}")
    print(f"Reverse ('Zebra', 'Lion'): {result_reverse}")