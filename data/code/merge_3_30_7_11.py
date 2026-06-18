def swap_adjacent_chars(s: str) -> None:
    """
    Iterates through a string represented as a mutable list of characters,
    swapping each character at index i with the character at index i+1 
    for all valid indices i. The operation is performed in-place on the internal representation.

    Args:
        s (str): A string input which will be converted to a list internally.
    
    Note:
        Since strings are immutable in Python, this function first converts 
        the input string into a list of characters before performing swaps.
    """
    # Convert the string to a mutable list for efficient modification
    char_list = list(s)

    # Iterate through the list up to n-1 (since we swap i with i+1)
    # We use range(len(char_list)) - 1 as valid indices go from 0 to len-2
    for i in range(len(char_list)):
        if i + 1 < len(char_list):
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]

def main():
    # Hard-coded sample values as per task requirements (no user input or files)
    sample_string = "Hello World"
    
    print("Original string:", " ".join(sample_string))
    
    swap_adjacent_chars(sample_string)
    
    new_str = "".join(sample_string)
    print("Swapped string: ", " ".join(new_str))

if __name__ == '__main__':
    main()