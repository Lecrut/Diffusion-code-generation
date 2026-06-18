def generate_substrings(text: str):
    """
    Generator function that yields all possible substrings of a given string.
    
    This implementation is memory-efficient as it does not build or store 
    any intermediate lists; instead, it generates each substring one by one.
    
    Args:
        text (str): The input string to generate substrings from.
        
    Yields:
        str: Each individual substring of the input text in order of starting index and length.
    """
    for start_index in range(len(text)):
        for end_index in range(start_index + 1, len(text) + 1):
            yield text[start_index:end_index]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    sample_string = "ABC"
    
    print("Generating substrings for:", repr(sample_string))
    count = 0
    
    try:
        while True:
            substring = next(generate_substrings(sample_string), None)
            if substring is not None:
                # Print the substring to verify generation. 
                # In a real large-scale scenario, one might write directly to a file or network stream instead of stdout.
                print(substring)
                count += 1
            
    except StopIteration:
        pass
    
    print(f"Total substrings generated for '{sample_string}': {count}")

    # Example with a longer string demonstrating the logic holds up, 
    # though it won't be printed fully due to length constraints in this demo context.
    long_sample = "ABCD"
    
    count_longer = 0
    
    try:
        while True:
            substring = next(generate_substrings(long_sample), None)
            if substring is not None:
                # Only print every nth item to prevent overwhelming output in a short script run, 
                # but the generator itself yields all efficiently.
                count_longer += 1
                
    except StopIteration:
        pass
    
    print(f"Total substrings generated for '{long_sample}': {count_longer}")