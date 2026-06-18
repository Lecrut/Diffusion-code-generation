"""
Script to concatenate words from a list of strings into a single string with no spaces between characters,
simulating line-by-line reading where each input is treated as part of the sequence.
Since interactive prompts and sys.stdin are disallowed per task constraints, this script uses 
a hard-coded sample block that mimics the logic for processing multiple lines of text 
and removing any existing spaces within or around words to achieve continuous concatenation.

Note: The specific request "no spaces between the words" combined with the prohibition
on input() suggests either joining a list by empty string (removing separators) or character-by-character removal.
Given typical interpretation in such constrained tasks without actual user data, 
we assume the goal is to join provided strings as if they were single-word tokens into one solid block of characters.

This script operates purely on static data within the main execution block.
"""

def remove_spaces_and_concatenate(word_list):
    """
    Concatenates a list of words by removing all space characters between them, 
    effectively merging adjacent strings without any whitespace.
    
    Parameters:
        word_list (list[str]): A list of string tokens representing 'lines' or 'words'.
        
    Returns:
        str: The concatenated result as a single continuous string with no spaces.
    """
    # Initialize empty result accumulator
    result = ""

    for current_word in word_list:
        if isinstance(current_word, str):
            result += current_word.replace(" ", "")
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values simulating line-by-line input that the function would process.
    # These are static strings representing what might be entered by a user if this were interactive.
    
    sample_inputs = [
        "Hello", 
        ", Welcome".replace(",", ""),  # Pre-cleaning example to simulate mixed content
        "# The quick brown"            # Example showing fragments that need joining
    
    ]

    final_output = remove_spaces_and_concatenate(sample_inputs) if sample_inputs else ""
    
    print(final_output)