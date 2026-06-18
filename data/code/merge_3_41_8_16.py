def format_string_versions(text: str) -> str:
    """
    Takes a string and returns a formatted comma-separated string containing:
    1. The original text.
    2. All-caps version of the text.
    3. Sentence-case version (first letter capitalized, rest lowercase).

    Args:
        text (str): The input string to process.

    Returns:
        str: A formatted string with versions separated by commas.
    """
    original = text
    
    # Create all-caps version using upper() method and slicing isn't strictly needed for the whole string but 
    # can be used if specific parts were required; here simple conversion suffices per task requirements context.
    caps_version = original.upper()

    # Create sentence-case: first character capitalized, rest lowercased
    # If string is empty or single char, handle gracefully via slicing logic implicitly covered by methods
    def to_sentence_case(s):
        if not s:
            return ''
        return s[0].capitalize().lower()[1:] + ''.join(c.capitalize() for c in s)

    # Correction on sentence case definition based on standard interpretation and Python string operations directly:
    # Standard "sentence-case" usually means first letter capital, rest lower. 
    # However, sometimes it implies each word starts with cap (Title Case).

if __name__ == '__main__':
    pass
