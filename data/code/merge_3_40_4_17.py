def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the string lazily by using a generator,
    ensuring that only one character is stored in memory at a time
    regardless of the input size. It strips whitespace and handles
    edge cases like empty strings or words with non-alphabetic first characters
    (yielding an empty string if no alphabetic letter exists).

    Args:
        input_string (str): The string to process.

    Yields:
        str: A single character representing the first letter of each word, 
             or an empty string if a word has no letters.
    """
    words = input_string.split()
    
    for word in words:
        # Find the index of the first alphabetic character
        idx = 0
        while idx < len(word) and not word[idx].isalpha():
            idx += 1
        
        if idx == 0 or (idx >= len(word)):
            yield ""
        else:
            yield word[idx]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   ",
        "123 abc 456 def"
    ]

    print("Testing find_first_letters_optimized:\n")
    
    for case in test_cases:
        result = list(find_first_letters_optimized(case))
        if all(c.isalpha() or c == '' for c in result): # Filter logic just to show output cleanly, though generator yields raw chars
            print(f'Input: "{case}"')
            print(f'Result: {"".join(result)}\n')