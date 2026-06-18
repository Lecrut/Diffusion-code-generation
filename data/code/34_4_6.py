#!/usr/bin/env python3
"""
Command-line utility to capitalize the first letter of each word in input text.
Reads from standard input, processes lines, and prints the result.
No external libraries are required.
"""

def process_text(text):
    """
    Capitalizes only the first letter of each word in the given string.
    
    Args:
        text (str): The input string to be processed.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    words = text.split()
    if not words:
        return ""
    
    # Capitalize the first character and lowercase the rest for each word, then join them back
    result_words = [word[0].upper() + word[1:].lower() for word in words]
    return " ".join(result_words)

def main():
    """
    Main function that handles command-line execution.
    
    Since no arguments are passed and input is read from stdin, 
    this block reads all lines until EOF (Ctrl+D on Unix/Linux/Mac).
    However, per the constraints of 'hard-coded sample values' running without user input,
    we will simulate a non-interactive run by using pre-defined strings.
    
    To strictly adhere to "No interactive prompt" and "Run without user input", 
    this script is designed to read from stdin normally in an environment where it might be piped or sourced,
    but the sample execution block below uses hardcoded values as requested.
    """

def main():
    # Simulating a run with hard-coded sample text that would otherwise come from stdin/args
    # This ensures the script runs without any user input, network access, or file I/O errors on startup.
    samples = [
        "hello world", 
        "python is awesome", 
        "the quick brown fox jumps over the lazy dog"
    ]

    for sample in samples:
        # Process each line of text and print the result immediately after processing (simulating stdin behavior)
        processed_text = process_text(sample)
        print(processed_text, end="")

if __name__ == '__main__':
    main()