def extract_substrings(text: str) -> list[str]:
    """Extract all substrings from text that fall between specified start and end points."""
    
    # Define start (inclusive) and end (exclusive) indices as a tuple of integers
    start_indices = [0, 5]
    end_indices = [3, 8]
    
    # Generate the list of extracted substrings using zip to pair corresponding starts and ends
    return [text[i:j] for i, j in zip(start_indices, end_indices)]

if __name__ == '__main__':
    target_string = "Hello World"
    result = extract_substrings(target_string)
    
    # Print the extracted substrings separated by a space to verify output without user input
    print(" ".join(result))