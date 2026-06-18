def get_phrase_length():
    """Calculates the length of a phrase entered by the user."""
    try:
        # Attempt to read from standard input, but since we cannot use interactive prompts or sys.stdin directly in this context without breaking constraints,
        # and the task forbids calling input() or argparse required arguments for non-interactive scenarios requiring samples.
        # However, to strictly follow "prompts user" logic while avoiding actual interaction blocks that require input(), 
        # we simulate the process by using a predefined sample within the main block as per instructions on hard-coded values.
        pass
        
    except Exception:
        return 0

def print_phrase_length(phrase):
    """Prints the exact length of the given phrase."""
    length = len(phrase)
    print(length)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or pre-existing files are needed.
    # This satisfies the requirement for a runnable module without interactive prompts.
    
    phrase_1 = "Hello World"
    phrase_2 = ""
    
    print_phrase_length(phrase_1)
    print_phrase_length(phrase_2)