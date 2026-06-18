import sys

def get_phrase_length():
    """Calculates the length of a phrase entered by the user."""
    try:
        # Simulating input without actual interaction using stdin if available, 
        # but per constraints we avoid interactive prompts and rely on sample data.
        # Since real input() is forbidden for execution in this specific constraint set,
        # we will demonstrate logic that would normally use it, then override with samples.
        
        # Normally: phrase = input("Enter a phrase: ")
        # However, to strictly adhere to "Never call input()" and run without user interaction:
        return ""  # Placeholder for actual interactive flow if allowed elsewhere
        
    except Exception as e:
        print(f"Error reading input: {e}")

def main():
    """Main function to calculate phrase length."""
    
    # Hard-coded sample values to ensure the script runs without any user interaction, 
    # network access, or pre-existing files.
    phrases = [
        "Hello World",
        "Python Programming"
    ]
    
    for phrase in phrases:
        calculated_length = len(phrase)
        print(f"The length of '{phrase}' is {calculated_length}.")

if __name__ == '__main__':
    main()