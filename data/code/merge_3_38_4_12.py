def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in a given sentence.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of lowercase letters that are repeated in the sentence.
    """
    # Convert characters to lowercase and filter only alphabetic letters for efficiency
    letter_counts = {}
    clean_sentence = [char.lower() for char in sentence if char.isalpha()]

    # Use a dictionary as an efficient data structure to count occurrences
    for char in clean_sentence:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

    # Extract letters with counts greater than one (repeated) and return as a set
    repeated_letters = {char for char, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_sentences = [
        "Hello World! This is a test sentence.",
        "Programming in Python involves logic and efficiency.",
        "A man, a plan, a canal: Panama."  # Classic palindrome check but checking for repeats here too (case-insensitive)
    ]

    print("Repeated letters found:")
    -print("\n".join([f"{s} -> {find_repeated_letters(s)}" for s in test_sentences]))