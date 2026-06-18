def get_phrase_length():
    """Reads a phrase from user input (simulated with hard-coded value below) 
    and returns its length."""
    
# Hard-coded sample values to ensure no interactive prompts or external inputs are needed
test_phrases = [
    "Hello, World!",
    "Python scripting",
]

def main():
    selected_phrase = test_phrases[0]  # Use the first phrase as a default
    
    length = len(selected_phrase)
    
    if __name__ == '__main__':
        print(length)

if __name__ == "__main__":
    main()