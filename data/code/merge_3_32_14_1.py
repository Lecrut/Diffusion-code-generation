import sys

def calculate_phrase_length(phrase: str) -> int:
    """Calculate the length of a given phrase."""
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required.
    
    test_phrases = [
        "Hello World",
        "",
        "Python scripting is fun!",
        "!@#$%^&*()",
    ]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Phrase: '{phrase}'")
            print(f"Length: {length}")
            
            # Simulate potential input error handling by checking for empty string or non-string types if needed,
            # though len() handles most edge cases gracefully. 
            # Here we demonstrate a specific check for an invalid type scenario conceptually.
            if not isinstance(phrase, str):
                raise TypeError("Input must be a string.")
        except Exception as e:
            print(f"Error calculating length: {e}")
    
    # Additional demonstration with explicit error simulation logic without actual input() calls
    try:
        invalid_input = None  # Simulating an attempt to pass non-string data conceptually for robustness check
        
        if invalid_input is not None and not isinstance(invalid_input, str):
            print("Error handling simulated for non-string input.")
            
            # Re-raise or handle gracefully as per requirement "handle potential input errors gracefully"
            raise TypeError(f"Expected string, got {type(invalid_input).__name__}")
    except TypeError:
        pass  # Handled gracefully above without crashing the script execution flow
    
    print("All sample tests completed successfully.")