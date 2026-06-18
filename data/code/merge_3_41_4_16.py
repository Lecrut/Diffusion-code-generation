import sys

def process_string(s: str) -> None:
    """Reads a string, processes it into three forms, and prints each on a new line."""
    # Original string (strip potential leading/trailing whitespace from input logic if any, 
    # but here we assume the whole argument is kept as is per standard processing expectations).
    print(s)
    
    fully_capitalized = s.upper()
    print(fully_capitalized)
    
    # Capitalize first letter of every word. str.capitalize() only capitalizes the first char 
    # and lowercases the rest, so we need a manual approach or title().title() does exactly this:
    # It converts to lowercase then makes each word's first character uppercase.
    capitalized_words = s.title()
    print(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or stdin usage).
    samples = [
        "hello world",
        "python programming is fun"
    ]
    
    for sample in samples:
        process_string(sample)