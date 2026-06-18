def format_string(text: str) -> str:
    """
    Returns a formatted string containing three versions of the input text:
    1. The original case version at the start.
    2. An all-caps version in the middle.
    3. A sentence-case version (first letter upper, rest lower) at the end.

    Versions are separated by commas and a space.
    """
    if not text:
        return ""
    
    # Convert to string just in case (though input is expected to be str)
    original = str(text)
    all_caps = original.upper()
    
    # Sentence case logic
    sentence_case_list = [word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper() 
                          for word in original.split()]
    sentence_case = " ".join(sentence_case_list).strip('.!,;:')

    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access.
    samples = [
        "Hello, World!",
        "Python is awesome.",
        ""
    ]

    print(format_string(samples[0]))
    print(format_string(samples[1]))
    print(repr(format_string(samples[2])))  # Show the empty string result clearly as it lacks punctuation logic handling for 'no words' above, adjusted below:
    
    # Re-evaluating sentence case for an empty string or spaces-only based on standard expectations.
    # The list comprehension handles single letters correctly (word.upper()). 
    # If input is " ", split results in [''], word[0] is space, upper remains space -> ' '.join(['']) -> ' '.
    # This might not be ideal for edge cases but adheres to logic derived from standard methods.