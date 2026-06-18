import sys

def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence character by character."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    # Sample 1: A normal sentence with punctuation and spaces.
    sample_1 = "Hello World!"
    
    # Sample 2: A longer sentence with mixed casing.
    sample_2 = "The quick brown fox jumps over the lazy dog."
    
    print("Reversed Sentence:")
    result_1 = reverse_sentence(sample_1)
    print(f"{sample_1} -> {result_1}")
    print("-" * 30)
    result_2 = reverse_sentence(sample_2)
    print(f"{sample_2} -> {result_2}")