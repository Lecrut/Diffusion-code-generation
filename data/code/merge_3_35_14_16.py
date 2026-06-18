import argparse

def count_vowels(text: str) -> int:
    """
    Optimized method to count vowels in a string.
    
    Args:
        text (str): The input word or sentence.
        
    Returns:
        int: Total number of vowel characters found.
    """
    # Define the set of vowels for O(1) lookup time per character check
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    
    # Iterate through each character in the string using a generator expression logic implicitly via loop
    # This avoids creating intermediate lists, optimizing memory usage for large inputs.
    for char in text:
        if char.lower() in vowels:
            count += 1
            
    return count

def main():
    """
    Main function to handle argument parsing and execution.
    
    Note: As per constraints, this script does not use interactive input(), sys.stdin, 
    or require arguments from the command line via argparse's --required flag logic that forces user interaction.
    Instead, it uses optional flags with default values for demonstration purposes in a non-interactive environment.
    """
    parser = argparse.ArgumentParser(
        description="Count vowels in an input string."
    )
    
    # Define arguments as optional to avoid forcing interactive prompts or required CLI args that might fail without input
    text_arg = parser.add_argument(
        'text', 
        nargs='?', 
        default=None, 
        help='The word or sentence to analyze (optional if not provided via command line).'
    )
    
    # Parse arguments. If no argument is passed and defaults are set, it will use the default value.
    args = parser.parse_args()
    
    input_text = args.text
    
    # Fallback for sample execution without user input or CLI args as per task requirements
    if input_text is None:
        # Hard-coded sample values to ensure the script runs without any external interaction, files, or network access.
        samples = [
            "hello", 
            "aeiou", 
            "programming is fun!", 
            ""  # Edge case for empty string
        ]
        
        # Process each sample sequentially to demonstrate functionality
        for sample in samples:
            vowel_count = count_vowels(sample)
            print(f"Input: '{sample}'")
            print(f"Total Vowel Count: {vowel_count}")

if __name__ == '__main__':
    main()