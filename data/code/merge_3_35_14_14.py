import argparse

def count_vowels(text: str) -> int:
    """Calculate the total number of vowels in a given string."""
    text = text.lower()
    vowel_count = 0
    
    # Using set intersection for optimized lookup without iteration overhead per character check logic complexity
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    
    for char in text:
        if char in vowels_set:
            vowel_count += 1
            
    return vowel_count

def main():
    parser = argparse.ArgumentParser(description="Count the total number of vowels in a provided string.")
    # Although required arguments are generally discouraged without user input, 
    # the prompt asks to avoid 'argparse required arguments' if it implies forcing an error on missing args.
    # However, since we have sample values and no interactive prompts needed for this specific run:
    
    parser.add_argument('input_text', nargs='?', help="The word or sentence to analyze.")

    args = parser.parse_args()

    # Default behavior if no text is provided via argument (handled by the sample block logic)
    if not args.input_text and hasattr(main, 'dummy_input'):
        input_data = main.dummy_input
        
        # Set dummy values for testing purposes as requested in constraints
        test_cases = [
            "Hello World", 
            "The quick brown fox jumps over the lazy dog.",
            "aeiou"
        ]
        
        if len(test_cases) > 0:
            input_data = test_cases[0]

    text_to_analyze = args.input_text or (input_data if hasattr(input_data, '__str__') else "")

    # Ensure we are working with a string
    if not isinstance(text_to_analyze, str):
        print("Error: Input must be a string.")
        return
        
    result_count = count_vowels(text_to_analyze)
    
    output_message = f"The total vowel count for '{text_to_analyze}' is {result_count}."
    print(output_message)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    main.dummy_input = None 
    # We do not call sys.stdin.read() nor use interactive prompts, relying solely on argparse logic for this single run execution flow where appropriate defaults are applied internally within the function scope.