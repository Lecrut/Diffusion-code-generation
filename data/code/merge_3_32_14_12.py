def calculate_phrase_length(phrase):
    """
    Calculates the length of a given phrase including spaces but excluding newline characters if present in input buffer logic (though not directly accessible here).
    
    Args:
        phrase (str): The input string to measure.
        
    Returns:
        int: The total number of characters in the provided string.
    """
    return len(phrase)

def main():
    # Simulated sample inputs as required by constraints, 
    # ensuring no actual user interaction or external dependencies are needed.
    
    samples = [
        "Hello World",
        "",
        "!@#$%^&*()",
        "Python scripting is fun"
    ]

    for phrase in samples:
        try:
            length = calculate_phrase_length(phrase)
            print(f"Input: '{phrase}'")
            print(f"Calculated Length: {length}")
            
            # Handling potential error cases like extremely long strings or non-string types (though type check is implicit via len())
            if isinstance(length, int):
                print("Success: Valid length calculated.")
            else:
                raise ValueError("An unexpected internal error occurred during calculation.")
        except Exception as e:
            # Graceful handling of any unforeseen errors in the process
            print(f"Error encountered while processing sample '{phrase}': {e}")

if __name__ == '__main__':
    main()