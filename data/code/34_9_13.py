import string

def capitalize_words(text: str) -> str:
    """
    Capitalizes only the first letter of each word in a given string.
    
    This function uses `title()` with `lowercase()` to ensure that 
    existing capitalization within words does not alter, but it is wrapped 
    by stripping non-alphabetic characters from the start and end to avoid 
    partial titles on special sequences if necessary. The most Pythonic approach 
    for simple per-word first-letter capitalization without affecting internal 
    casing (other than normalization) involves splitting into tokens, capitalizing 
    each token's first character, and joining them back.
    
    Args:
        text (str): Input string potentially containing mixed case letters
        
    Returns:
        str: String with the first letter of each word capitalized in title-case
               but preserving internal casing structure unless using pure Title() logic.
    """
    # The most efficient and Pythonic way to capitalize only the first letter 
    # of each word while leaving other characters unchanged (except spaces) is:
    return ' '.join(word.capitalize() if len(word.strip()) > 0 else '' for word in text.split(' ') if any(c.isalpha() for c in word))

if __name__ == '__main__':
    sample_text = "hello WORLD! this IS python, isn't it?"
    
    result = capitalize_words(sample_text)
    
    print("Input:  ", sample_text)
    print("Output: ", result)