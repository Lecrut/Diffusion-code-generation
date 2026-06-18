def format_strings(text: str) -> str:
    """
    Takes a string and returns a formatted string containing three versions:
    1. The original text.
    2. All uppercase version of the text.
    3. Sentence case version of the text (first letter capitalized, rest lowercase).

    Uses slicing and built-in methods to achieve this transformation.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A comma-separated string with original, uppercase, and sentence-case versions.
    """
    # Create the all-caps version using upper() method
    caps_version = text.upper()
    
    # Convert to lowercase first, then capitalize each word for sentence case logic
    # Split by spaces or punctuation that might act as separators if needed, 
    # but standard 'capitalize' only handles start of string.
    # To make a robust "sentence-case" (first letter cap, rest lower), we can:
    # 1. Lowercase the whole string
    # 2. Capitalize the first character
    
    lowercase_text = text.lower()
    
    if len(lowercase_text) == 0:
        sentence_version = ""
    else:
        # Slice to get first char, slice from index 1 for rest
        first_char = lowercase_text[0].upper()
        remaining_chars = lowercase_text[1:]
        sentence_version = first_char + remaining_chars
    
    return f"{text}, {caps_version}, {sentence_version}"

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or file access is needed
    samples = [
        "hello world",
        "Python 3.9 Is Great!",
        ""
    ]

    for s in samples:
        result = format_strings(s)
        print(result)