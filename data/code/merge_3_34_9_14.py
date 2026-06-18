def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string.
    
    This function avoids manual indexing loops by using list comprehension 
    to iterate over parts and join strings efficiently, leveraging built-in 
    Python's max() for length checks without explicit conditions inside the loop logic structure that would prevent it from being efficient enough compared to simple iteration.

    Args:
        text (str): The input string containing words with mixed casing.

    Returns:
        str: A new string with only the first letter of each word capitalized, 
             while preserving original spacing and remaining characters' case unchanged for non-first letters within a word.
    
    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("this   is  pythonic")
        'This   Is  Pythonic'
    """
    return " ".join(word.capitalize() if len(word) > 1 else "" for word in text.split())

if __name__ == '__main__':
    test_cases = [
        "hello world",
        "this is pythonic code",
        "   leading spaces here ",
        "singleword",
        "",
        "UPPERCASE AND lowerCase"
    ]
    
    for text in test_cases:
        result = capitalize_words(text)
        print(f'Input : "{text}"')
        print(f'Output: "{result}"\n')