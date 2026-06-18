import sys

def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence efficiently using string slicing."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    # Simulate prompts and inputs for demonstration purposes only; no actual I/O occurs.
    print("Enter a sentence (this will use a hard-coded value instead):")
    
    sample_sentence = "Hello World"  # Hard-coded input
    
    reversed_sentence = reverse_sentence(sample_sentence)
    
    print(f"\nOriginal: {sample_sentence}")
    print(f"Reversed: {reversed_sentence}")