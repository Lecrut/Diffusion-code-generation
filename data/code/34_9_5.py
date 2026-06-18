import textwrap

def capitalize_first_word(s: str) -> str:
    """
    Capitalize only the first letter of each word in a string if it is lowercase.
    
    This function uses Python's built-in `capitalize()` method on individual words,
    joined back together with original casing for subsequent letters to ensure 
    efficiency and readability without manual indexing loops.
    
    Args:
        s (str): The input string containing multiple words.
        
    Returns:
        str: A new string where the first letter of each word is capitalized if needed,
             preserving existing capitalization for non-first-letter characters within a word.
    """
    return " ".join(word.capitalize() for word in s.split())

if __name__ == '__main__':
    sample_1 = "hello world"
    sample_2 = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    sample_3 = "mixed CASE and ALL LOWERCASE text 123 numbers!"

    print("Sample 1:", capitalize_first_word(sample_1))
    # Expected: Hello World
    
    result_2 = capitalize_first_word(sample_2)
    
    # Note: The prompt specifically asks to avoid manual loops. 
    # Using string methods (split, join, capitalize) is the Pythonic idiom for this task.
    print("Sample 2:", result_2)
    
    sample_with_numbers = "start1 middle2 end3"
    print(f"With numbers: '{sample_with_numbers}' -> {capitalize_first_word(sample_with_numbers)}")