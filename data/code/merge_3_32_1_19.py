def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string phrase.
    
    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: The length of the string in characters.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or file I/O
    samples = [
        "Hello, World!",
        "",
        "Python is optimized and efficient.",
        "A" * 1000,
        "\n\t\x0bSpecial characters: tab\n",
    ]

    print("Testing calculate_phrase_length function:")
    for i, sample in enumerate(samples):
        length = calculate_phrase_length(sample)
        # Use repr to show non-printable chars if any, though len() counts them correctly too
        display_str = str(sample)[:50] + "..." if len(str(sample)) > 50 else str(sample)
        print(f"Sample {i+1}: Length={length}, Content='{display_str}'")