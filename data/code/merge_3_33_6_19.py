import sys

def main():
    # Generate sample data directly within the script to ensure it runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    sample_data = [
        "Hello",
        "World",
        "This",
        "Is",
        "A",
        "Test"
    ]

    concatenated_result = ""
    
    for word in sample_data:
        # Remove any existing whitespace from the beginning or end of each string before concatenating.
        clean_word = word.strip()
        if not clean_word:
            continue
        
        # Append to result without adding spaces between words as per requirements.
        concatenated_result += clean_word

    print(concatenated_result)

if __name__ == '__main__':
    main()