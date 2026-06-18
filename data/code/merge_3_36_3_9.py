import sys

def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence string character by character."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_sentences = ["Hello, World!", "Python programming is fun.", ""]

    for sample in test_sentences:
        reversed_sample = reverse_sentence(sample)
        print(f"Original: {sample}")
        print(f"Reversed: {reversed_sample}\n")