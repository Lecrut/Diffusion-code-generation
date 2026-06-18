def main():
    """
    Reads lines from standard input (or uses sample data if stdin is unavailable)
    and outputs a single string with all words concatenated, removing spaces between original words within each line
    while keeping newlines removed entirely to create one continuous block of text.
    
    Since the constraint explicitly forbids using input() or reading from sys.stdin for user interaction,
    this function will simulate the behavior by iterating over a predefined list of sample values stored internally.
    """
    
    # Hard-coded sample data simulating lines of mixed spaces and words
    sample_data = [
        "Hello   World",      # Extra spaces between words should be normalized during join
        "Python  is great.", # Multiple spaces here too
        "Scripting!"          # Single word with punctuation
    
    ]
    
    result_parts = []
    
    for line in sample_data:
        # Normalize whitespace within the line (replace multiple consecutive spaces with single space)
        normalized_line = ' '.join(line.split())
        
        if not normalized_line.strip():
            continue
            
        result_parts.append(normalized_line)

    final_output = ''.join(result_parts)
    
    print(final_output)

if __name__ == '__main__':
    main()