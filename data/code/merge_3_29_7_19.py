def reverse_string_in_place(s: str) -> str:
    """
    Reverses a string in-place using minimal memory by converting it to a list of characters,
    swapping from both ends towards the center, and joining back into a single string.
    
    This approach minimizes memory usage relative to creating new strings during iteration 
    or slicing operations (which create copies). It avoids intermediate large allocations 
    except for the initial conversion to a mutable sequence and final join operation.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    # Convert string to list of characters as strings are immutable in Python,
    # allowing us to modify elements without creating new objects for each character change.
    char_list = list(s)
    
    left_index = 0
    right_index = len(char_list) - 1
    
    while left_index < right_index:
        # Swap characters at both ends moving towards the center
        temp_char = char_list[left_index]
        char_list[left_index] = char_list[right_index]
        char_list[right_index] = temp_char
        
        left_index += 1
        right_index -= 1
    
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        "hello",
        "",
        "a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z",
        "Python Programming is Fun!",
        "1234567890"
    ]

    for test_input in test_cases:
        reversed_result = reverse_string_in_place(test_input)
        print(f"Original: '{test_input}'")
        print(f"Reversed: '{reversed_result}'\n")