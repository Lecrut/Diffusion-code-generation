def process_string(text):
    """Convert a string to lowercase, uppercase, and title case."""
    return {
        'lowercase': text.lower(),
        'uppercase': text.upper(),
        'title_case': text.title()
    }

if __name__ == '__main__':
    sample_input = "Hello World"
    
    results = process_string(sample_input)
    
    print(f"{sample_input} -> Lowercase: {results['lowercase']}")
    print(f"{sample_input} -> Uppercase: {results['uppercase']}")
    print(f"{sample_input} -> Title Case: {results['title_case']}")