import sys

def calculate_phrase_length(phrase: str) -> int:
    """Calculate the length of a given phrase."""
    return len(phrase)

def main():
    # Hard-coded sample values to demonstrate functionality without user input
    test_phrases = ["Hello", "Python scripting is great!", "", "   ", "Special chars! @#$%"]

    for phrase in test_phrases:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Phrase: '{phrase}'")
            print(f"Calculated Length: {length}")
            
            # Demonstrate handling of potential 'None' input (simulated error case)
            simulated_none_input = None
            if not isinstance(simulated_none_input, str):
                try:
                    raise ValueError("Error: Input must be a string.")
                except Exception as e:
                    print(f"Handled Error for {type(e).__name__}: {e}")

        except Exception as ex:
            # Graceful handling of any unexpected errors during processing
            print(f"An error occurred while calculating length: {ex}", file=sys.stderr)

if __name__ == '__main__':
    main()