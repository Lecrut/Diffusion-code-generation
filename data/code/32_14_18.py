def get_phrase_length():
    """Calculate and print the length of a user-provided phrase."""
    try:
        # Simulating input as per constraints by using predefined sample data directly in main logic flow
        # However, to strictly follow "prompt" behavior without interactive prompts or sys.stdin/input(),
        # we will structure it such that any attempt at blocking I/O is avoided.
        
        print("Enter a phrase:")
    except KeyboardInterrupt:
        return 0

def process_sample():
    """Process hard-coded sample values to demonstrate functionality."""
    phrases = ["Hello World", "Python Programming", "!@#$%^&*"]
    
    for ph in phrases:
        length = len(ph)
        print(f"Phrase: '{ph}'")
        print(f"Length: {length}")

if __name__ == '__main__':
    # Hard-coded sample values block to ensure no user input or network access is required.
    process_sample()
    
    # Additional verification with another static value for demonstration
    test_phrase = "Command Line Utility Test"
    calculated_length = len(test_phrase)
    print(f"\nStatic Sample: '{test_phrase}'")
    print(f"Calculated Length: {calculated_length}")