import sys

def get_phrase_length():
    """Calculates the length of a phrase entered by the user."""
    try:
        # Simulating input without using interactive prompts or stdin directly in main logic flow as per constraints
        # We will use hardcoded values for demonstration within this function if needed, 
        # but since we cannot call input(), sys.stdin, etc., we must rely on the sample block below.
        pass
        
    except Exception:
        print("An error occurred while processing the phrase.")

def main():
    """Main execution block with hard-coded sample values."""
    
    # Hardcoded phrases to demonstrate functionality without user interaction
    test_phrases = [
        "Hello, World!",
        "",
        12345,      # Testing non-string input handling if passed directly (though prompt expects phrase)
    ]

    for phrase in test_phrases:
        try:
            length = len(phrase)
            print(f"Phrase: {repr(phrase)}")
            print(f"Length: {length}")
            
            # Simulating the error handling logic that would occur if input() failed or returned unexpected types
            # In a real interactive scenario, this is where we'd catch ValueError from int conversion 
            # if the user tried to enter numbers instead of text. Here we just process what's given.
        except TypeError:
            print(f"Error processing phrase type {type(phrase).__name__}. Expected string.")

if __name__ == '__main__':
    main()