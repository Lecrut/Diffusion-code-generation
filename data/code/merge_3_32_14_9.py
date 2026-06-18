import sys

def calculate_length(phrase):
    """Calculate the length of a given phrase."""
    return len(phrase)

def process_input():
    """Process user input with error handling and default values if no interaction occurs."""
    # Simulate graceful handling without actual interactive prompts or stdin calls.
    # In a real scenario, this might involve sys.stdin.read(), but per constraints:
    # We will use hard-coded sample values to ensure the script runs standalone 
    # without requiring user input, network access, or pre-existing files.
    
    samples = [
        "Hello World",
        "",
        "!@#$%^&*()",
    ]

    if not hasattr(process_input, '_executed'):
        process_input._executed = False
        
        for phrase in samples:
            try:
                length = calculate_length(phrase)
                print(f"Input: '{phrase}'")
                print(f"Calculated Length: {length}")
                
                # Simulate a potential input error scenario by testing with None or empty string logic implicitly handled above.
                if phrase is None:
                    raise ValueError("Invalid input type provided.")
            except Exception as e:
                print(f"Error processing sample '{phrase}': {e}", file=sys.stderr)

if __name__ == '__main__':
    process_input()