"""
Module to capitalize the first letter of each word in a string efficiently 
without manual indexing loops, adhering to Pythonic conventions.
"""

def capitalize_words(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the input string.
    
    This function uses list comprehension and the built-in `capitalize()` method
    on strings within a split/join operation, which is more efficient than 
    manual indexing loops for typical use cases involving standard ASCII or Unicode text.

    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    samples = [
        "hello world",
        "python is awesome",
        "the quick brown fox jumps over the lazy dog",
        "single word case"
    ]

    for original in samples:
        result = capitalize_words(original)
        print(f'Original: "{original}"')
        print(f'Result:   "{result}"\n')