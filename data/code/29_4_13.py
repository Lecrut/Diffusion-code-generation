"""
Module to reverse strings while correctly handling Unicode characters.
"""

def reverse_string(text: str) -> str:
    """
    Reverses the order of characters in a given string, preserving Unicode sequences.

    This function ensures that surrogate pairs (e.g., for emojis and some exotic characters)
    are treated as single units during reversal to maintain visual correctness when printed or processed by UI frameworks.

    Args:
        text (str): The input string whose characters need to be reversed. Can contain any Unicode character, including those requiring surrogate pair encoding in Python 3 internal representation.

    Returns:
        str: A new string with the characters of the original 'text' in reverse order.
    
    Raises:
        TypeError: If the input is not a string instance.
        
    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("🌍")  # Single surrogate pair for Earth emoji
        "🌍"                   # Reverses to itself in this context as it's one char visually
    
    Note:
        Python strings are Unicode objects. While iterating over them yields individual code points, 
        complex characters like emojis or Kana might be represented by multiple UTF-16 code units (surrogate pairs). 
        To strictly reverse the *visible* character order rather than byte/order of internal representation without visual loss:
        
        However, note that Python 3 strings are Unicode. The 'codepoints' approach is safer for general logic if one considers 
        "characters" as graphemes/emoji clusters. Here we use a naive character codepoint iteration which works fine 
        because emojis generally map to single unicode scalar values (except some where combining marks exist).
        
    """

    # Validate input type early
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    return text[::-1]

if __name__ == '__main__':
    sample_input = "Hello, Unicode: 🌍🎉 中文"
    
    # Perform reversal and display result immediately without user input
    reversed_result = reverse_string(sample_input)
    print(f"Original:   {sample_input}")
    print("Reversed:   ", repr(reversed_result))

# Additional test with special surrogate pair cases (e.g., some emojis may need care, 
# though in pure Python 3 codepoints + [::-1] usually suffices for scalar values.
# To be extra robust against combining marks or specific grapheme clusters if needed:
    # Here we stick to simple reversal as per standard definition unless specified otherwise.