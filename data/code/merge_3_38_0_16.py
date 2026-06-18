def find_repeated_letters(text: str) -> list[str]:
    """
    Takes a string as input and checks for any repeated letters within that string,
    returning a list of unique characters found more than once (case-insensitive).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of uppercase letters that appear multiple times in the input.
    """
    # Convert to lowercase for case-insensitive comparison and filter out non-alphabetic characters
    filtered_text = [char.lower() for char in text if char.isalpha()]
    
    frequency_map = {}
    repeated_letters = []

    for letter in filtered_text:
        count = frequency_map.get(letter, 0) + 1
        # If the character hasn't been added to our list yet and its count is now > 1
        if count == 2 or (count > 2 and letter not in repeated_letters):
            repeated_letters.append(letter)
            
    return sorted(repeated_letters)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    test_cases = [
        "Hello World!",
        "Python Programming",
        "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
        "No repeated letters here 123 !@#",
    ]

    for test_input in test_cases:
        result = find_repeated_letters(test_input)
        if result:
            print(f"Input: '{test_input}'")
            print(f"Repeated letters found: {', '.join(result)}\n")
        else:
            print(f"No repeated letters found for input: '{test_input}'\n")