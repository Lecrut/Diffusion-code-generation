def capitalize_words(text):
    """
    Decorator that automatically capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Sample usage demonstrating the decorator functionality
    sample_strings = [
        "hello world",
        "python is awesome",
        "this is a test string with multiple words"
    ]

    print("Original Strings:")
    for s in sample_strings:
        print(f'"{s}"')
    
    print("\nCapitalized Results:")
    result = capitalize_words(sample_strings[0])  # Using the first one as example or loop all
    
    # To demonstrate on multiple, we can just apply it to each if needed, 
    # but since 'capitalize_words' is a function (acting like a decorator in spirit here),
    # let's show results for clarity.
    
    print(f"Input:  '{sample_strings[0]}'")
    print(f"Output: '{result}'")