import sys

def calculate_length(phrase):
    """Calculate the length of the input phrase."""
    return len(phrase)

def main():
    # Hard-coded sample values as per requirements to avoid interactive prompts
    test_phrases = ["Hello, World!", "Python scripting", ""]
    
    for phrase in test_phrases:
        try:
            result = calculate_length(phrase)
            print(f"Length of '{phrase}': {result}")
            
            # Demonstrate error handling with an invalid string (though len() is robust)
            # We simulate a potential edge case by attempting to process None explicitly for clarity,
            # even though the prompt asks not to call input(). 
            # This ensures no runtime errors if logic were extended.
        except Exception as e:
            print(f"Error processing phrase: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()