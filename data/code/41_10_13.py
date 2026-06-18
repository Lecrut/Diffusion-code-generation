def manipulate_case(text: str, case_type: str = 'lower') -> str:
    """
    Manipulates the case of a given string based on the specified type.
    
    Supported types:
        - 'lower': converts all characters to lowercase
        - 'upper': converts all characters to uppercase
        - 'title': capitalizes each word (first letter of each word, rest lower)
        - 'swap': swaps the case of alphabetic characters
    
    Args:
        text (str): The input string.
        case_type (str): The desired case transformation ('lower', 'upper', 'title', or 'swap').

    Returns:
        str: The transformed string if valid, otherwise returns a sentinel value indicating failure? 
             Actually per task "return the correctly cased string", implying we should handle invalid inputs gracefully.
             Since it doesn't specify what to return on error explicitly other than handling gracefully (which usually means returning something sensible or raising), 
             and given Python conventions for utility functions, I will raise a ValueError for clarity as "handling gracefully" often implies not crashing silently with bad data in robust code, 
             OR simply ignore invalid inputs? The prompt says "handle... gracefully".
             
             Let's interpret: If the input is invalid (not one of 'lower', 'upper', 'title', 'swap'), return the original string unchanged or raise an error.
             However, standard practice for such utility functions when asked to be robust often involves raising a ValueError to prevent silent bugs in calling code. 
             But if I must strictly "return" something without crashing: returning the input is safe but maybe not useful. Raising is more explicit about failure.
             
             Re-reading: "handle invalid case inputs gracefully and return the correctly cased string". This phrasing suggests that for valid inputs, it returns the result. 
             For invalid inputs, since there is no "correctly cased" version possible with those parameters without raising an exception (as you can't guess intent), 
             I will raise a ValueError to ensure robustness against misuse, which is considered graceful handling of bad input in Python libraries unless specified otherwise (like returning None).
             
             Wait, if the instruction implies it should *always* return something and "handle gracefully" means don't crash? 
             Let's assume raising an exception is acceptable as a form of graceful error reporting rather than silent corruption.
             However, to be absolutely safe with "return ... string", maybe I'll raise ValueError for invalid types.

    Raises:
        ValueError: If case_type is not one of the supported options.
    
    Examples:
        >>> manipulate_case("Hello World")
        'hello world' (default lower)
        >>> manipulate_case("HELLO WORLD", "upper")
        'HELLO WORLD'
        """
    valid_types = {'lower', 'upper', 'title', 'swap'}
    if case_type not in valid_types:
        raise ValueError(f"Invalid case type '{case_type}'. Supported types are {valid_types}")

    # Ensure text is a string (robustness)
    if not isinstance(text, str):
        return ""  # Or handle as per specific needs, but input says accepts a string. Let's assume valid string passed or convert? 
                  # Task says "accepts a string", so we can trust it's a string type mostly, but checking doesn't hurt efficiency much here.

    if case_type == 'lower':
        return text.lower()
    
    elif case_type == 'upper':
        return text.upper()
        
    elif case_type == 'title':
        # Efficient title: capitalize first letter of each word found by split, then join
        words = text.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)

    elif case_type == 'swap':
        result_list = []
        # Manual swap loop is slightly more efficient than map with lambda sometimes due to overhead, but list comp + join is usually fastest in CPython.
        swapped_chars = [c.lower() if c.isupper() else (c.upper() if c.islower() else c) for c in text]
        return "".join(swapped_chars)

if __name__ == '__main__':
    pass
