import sys

def get_phrase_length(phrase):
    """Calculate the length of a given phrase."""
    return len(str(phrase))

def main():
    # Hard-coded sample values to ensure the script runs without user input
    samples = ["Hello", "Python programming is fun!", "", "Spaces and tabs  "]
    
    for i, test_phrase in enumerate(samples):
        result = get_phrase_length(test_phrase)
        print(f"Sample {i}: '{test_phrase}' -> Length: {result}")

if __name__ == '__main__':
    main()