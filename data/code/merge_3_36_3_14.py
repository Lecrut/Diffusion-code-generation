def main():
    """
    Prompts the user to enter a sentence (simulated with hardcoded value)
    and prints the reversed sentence to the console.
    
    This function includes both an interactive prompt scenario and 
    hard-coded sample values for demonstration purposes as per requirements.
    However, to strictly adhere to "Never call input()", sys.stdin, or any interactive prompt,
    this module will only utilize the hard-coded sample value logic in its execution block.
    """

    # Hardcoded sample sentence to demonstrate functionality without user interaction
    SAMPLE_SENTENCE = "Hello World"

    def reverse_sentence(sentence: str) -> str:
        """Reverses the given string."""
        return sentence[::-1]

    if __name__ == '__main__':
        # Process only the hardcoded sample value to ensure no input() or interactive prompts are called
        original = SAMPLE_SENTENCE
        reversed_text = reverse_sentence(original)
        
        print(f"Original: {original}")
        print("Reversed:")
        print(reversed_text)