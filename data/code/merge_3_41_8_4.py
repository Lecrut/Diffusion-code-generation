def format_string(s: str) -> str:
    """
    Creates a formatted string containing three versions of the input string,
    separated by commas: original, all-caps, and sentence-case.
    
    Uses slicing to reverse words for sentence case logic if needed, 
    but primarily relies on built-in methods like upper(), lower().split()[-1].capitalize().join().lower()

    Args:
        s (str): The input string.
        
    Returns:
        str: A comma-separated string of [original, all-caps, sentence-case].
    """
    original = s
    
    # All caps version using upper method
    all_caps = original.upper()
    
    # Sentence case logic: 
    # 1. Split into words (handling multiple spaces by filtering)
    # 2. Capitalize the first letter of each word, lower-case the rest
    # 3. Join them back together
    sentence_case_words = [word[0].upper() + word[1:].lower() for word in original.split()] 
    sentence_case = ' '.join(sentence_case_words)

    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network access)
    samples = ["hello world", "python programming is fun!", "  multiple   spaces  test"]
    
    for item in samples:
        result = format_string(item)
        print(result)