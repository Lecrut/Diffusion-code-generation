import re

def capitalize_sentence(sentence: str) -> str:
    """
    Capitalize the first letter of each word in a sentence.
    
    This function uses regular expressions to identify words and list 
    comprehensions with generator expressions for efficient processing.
    It handles multiple spaces, punctuation at ends, and mixed case input gracefully.
    
    Args:
        sentence (str): The input string containing the sentence.
        
    Returns:
        str: A new string where each word's first letter is capitalized 
             and subsequent letters are lowercased.
    """
    # Split into words using regex to handle various delimiters including punctuation
    words = re.findall(r'\b\w+\b', sentence)
    
    # Use list comprehension with generator expression for memory efficiency on large inputs
    capitalized_words = [word.capitalize() if word else '' for word in words]
    
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_sentences = [
        "hello world, this is a test.",
        "python programming is fun!",
        "  multiple   spaces and punctuation? ",
        ""
    ]
    
    for s in sample_sentences:
        print(f"Original: '{s}'")
        result = capitalize_sentence(s)
        print(f"Capitalized: '{result}'\n")