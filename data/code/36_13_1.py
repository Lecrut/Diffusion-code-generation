import sys

def reverse_sentence(sentence):
    """
    Reverses a given sentence using efficient string slicing.
    
    Args:
        sentence (str): The input sentence to be reversed.
        
    Returns:
        str: The reversed sentence.
    """
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction or prompts used.
    test_sentences = [
        "Hello, World!",
        "Python is powerful.",
        "The quick brown fox jumps over the lazy dog."
    ]
    
    for sentence in test_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")

# Suppress any potential stderr output from sys.exit if used elsewhere, though not needed here.
sys.stderr.write("No user input required; all samples processed.\n")