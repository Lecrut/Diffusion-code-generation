def reverse_sentence(sentence: str) -> str:
    """
    Reverses a given sentence efficiently by slicing.
    
    Args:
        sentence (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user interaction or external inputs used.
    test_sentences = [
        "Hello, world!",
        "Python programming is fun.",
        "",
        "A man a plan a canal Panama!"
    ]

    for sentence in test_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed:{reversed_sentence}\n")