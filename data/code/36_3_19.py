import sys

def reverse_sentence():
    """Prints a sentence reversed to the console."""
    sample_input = "Hello World!"
    
    # Process the hard-coded sample value as if it were user input
    sentence_to_reverse = " ".join(sample_input)  # Normalize spaces for cleaner reversal output
    
    print(sentence_to_reverse[::-1])

if __name__ == '__main__':
    reverse_sentence()