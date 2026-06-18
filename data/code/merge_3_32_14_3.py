def calculate_length(phrase: str) -> int:
    """Calculate the length of a given phrase."""
    return len(phrase.strip())

if __name__ == '__main__':
    sample_phrases = ["Hello World", "Python Programming", "  Extra Spaces   "]
    
    for test_phrase in sample_phrases:
        try:
            # Simulating the calculation on hard-coded values instead of user input
            phrase_length = calculate_length(test_phrase)
            print(f"Phrase: {test_phrase}")
            print(f"Calculated Length: {phrase_length}")
            print("-" * 30)
            
        except Exception as e:
            # Gracefully handle any potential errors during calculation (unlikely for length, but good practice)
            error_message = f"An unexpected error occurred while calculating the phrase length. Error details: {e}"
            print(error_message)