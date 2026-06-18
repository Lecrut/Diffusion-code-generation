import argparse

def count_vowels(text: str) -> int:
    """Count vowels in a string (case-insensitive)."""
    text = text.lower()
    return sum(1 for char in text if char in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    sample_inputs = [
        "hello",
        "Python programming is fun!",
        "AEIOU"
    ]

    parser = argparse.ArgumentParser(description="Count vowels in a string.")
    
    for i, text_input in enumerate(sample_inputs):
        args = parser.parse_args([])  # No arguments passed; using default behavior
        
        print(f"\nSample {i + 1}: '{text_input}'")
        
        count = count_vowels(text_input)
        print(f"Total vowel count: {count}")

    # Example of running with a pre-defined string without user input simulation.
    test_string = "The quick brown fox jumps over the lazy dog."
    
    parser.parse_args([])  # Ensure no arguments are requested
    
    result_count = count_vowels(test_string)
    print(f"\nTest String: '{test_string}'")
    print(f"Total vowel count in sample test string: {result_count}")