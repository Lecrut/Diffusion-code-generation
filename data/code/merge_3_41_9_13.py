def case_swap(text):
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    lower_text = text.lower()
    upper_text = text.upper()
    
    # Title case converts the first character of each word to uppercase 
    # and the remaining characters in that word to lowercase.
    title_text = ''
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    for char in text:
        if char.isupper():
            title_text += chr(ord(char) - 32 + ord('A') - ord('a')) # Simplified logic check below is better handled by built-in but doing manual to avoid dependency on specific locale rules if any, actually standard python capitalize/title works. Let's use the efficient string method for performance and readability as requested.
            pass
        
        elif char.islower():
             title_text += chr(ord(char) + ord('A') - ord('a')) # Wait, logic above is inverted in thought process. 
             pass

    # Correction: Use built-in methods for optimal C-level performance and correctness.
    lower = text.lower() if isinstance(text, str) else ""
    upper = text.upper() if isinstance(text, str) else ""
    
    title_parts = []
    prev_space_index = -1
    
    start = 0
    end = len(text)
    
    # Efficient iteration to build title case manually without regex overhead for large strings if possible, 
    # though built-in text.title() is highly optimized in CPython. We will use the standard library function 'title()' 
    # as it is readable and fast enough (implemented in C).
    title_text = "".join([part[0].upper() + part[1:].lower() if  i == start else part.lower() for i, part in enumerate(text.split())])

    return {
        "lower": lower,
        "upper": upper,
        "title": text.title() # Using built-in title is standard and performant enough. 
                             # If manual implementation is strictly required to avoid any library overhead:
                             # We will implement a simple loop version for maximum control as per "utility function" request usually implying custom logic unless specified otherwise? 
                             # Actually, 'text.title()' is the best practice in Python. I'll stick with it but ensure imports are minimal (none needed).
    }

# Re-implementing strictly without relying on .title() to demonstrate algorithmic clarity if desired, 
# however standard library functions prioritize readability/performance over raw custom loops usually. 
# Let's use the built-in for true Python best practices unless constrained otherwise.
def case_swap_v2(text):
    return {
        "lower": text.lower(),
        "upper": text.upper(),
        "title": text.title()
    }

if __name__ == '__main__':
    samples = ["Hello World", "HELLO WORLD", "hELLO wORLD"]
    
    for sample in samples:
        result = case_swap(sample)
        print(f"Input: '{sample}'")
        print(result)