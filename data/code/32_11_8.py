def calculate_phrase_length(phrase: str) -> int:
    """
    Returns the length of a string phrase as an integer.
    
    This function uses Python's built-in len() which is implemented in C,
    making it highly efficient (O(n)) for counting characters without iterating
    manually or allocating additional memory structures.

    :param phrase: A single input string representing the phrase to measure.
    :return: The integer length of the provided string.
    """
    return len(phrase)

if __name__ == '__main__':
    sample_phrases = [
        "Hello",
        "",
        "Python is optimized.",
        "A" * 1000,
    ]

    for phrase in sample_phrases:
        result = calculate_phrase_length(phrase)
        print(f"'{phrase}' -> {result}")