def get_first_letters(text):
    # Create a list to hold the cleaned parts (alphanumeric sequences)
    result = []
    for part in text.split():
        # Filter only alphanumeric characters from start until hit non-alnum? 
        # Or simpler: replace all non-alnums with space first globally then split.
        pass

# Let's write it properly using string translation or iteration to avoid regex if we want zero dependencies,
# but `re` is standard library and efficient for this specific task of isolating words.
import re

def get_first_letters(text: str) -> list[str]:
    """Returns a list containing the first letter of every word in the input string."""
    
    # Split into tokens that are purely alphanumeric sequences to handle punctuation gracefully (e.g., "word," vs "word")
    words = re.findall(r'\b[\w]+', text) 
    return [word[0] if word else '' for word in words]

if __name__ == '__main__':
    sample_strings = [
        "Hello, world! This is a test.",
        "Don't forget to smile. It's good!",
        "One two three four five",
        "Python 3.x is great."
    ]
    
    for s in sample_strings:
        # The input string might have no words? 
        output = get_first_letters(s)
        print(f"Input: '{s}'")
        print(f"Output: {output}")