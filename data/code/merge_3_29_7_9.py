import sys

def reverse_string_memory_efficient(s: str) -> str:
    """
    Reverses a string by converting it to a list of characters, reversing in-place,
    and joining back into a string. This approach minimizes memory usage compared 
    to creating intermediate concatenated strings or slices that duplicate data.

    Args:
        s (str): The input string to reverse.

    Returns:
        str: The reversed string.
    
    Explanation of Approach:
    Strings in Python are immutable, meaning any operation like slicing (e.g., 
    s[::-1]) creates a new string object, effectively duplicating the data. To minimize memory usage,
    we convert the string to a list of characters (which is mutable), reverse this list using two-pointer logic
    or built-in reversal without creating temporary slices, and then join it back into a single string result.
    This avoids intermediate large string allocations during the process.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(n) for storing characters in the list (inevitable since strings are immutable), 
    but significantly less memory overhead than repeated slicing and concatenation strategies which create multiple copies.
    """
    # Convert string to a mutable list of characters
    char_list = list(s)
    
    # Use two-pointer approach to reverse in-place without auxiliary lists/slices
    left, right = 0, len(char_list) - 1
    
    while left < right:
        # Swap elements at current pointers
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
        
    # Join the list back into a string for return (necessary step as lists cannot be returned directly)
    return ''.join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies are required.
    samples = [
        "hello",
        "",
        "a man a plan a canal Panama!",  # Includes spaces and special characters
        "Python is awesome.",
        "1234567890"
    ]

    for sample in samples:
        reversed_result = reverse_string_memory_efficient(sample)
        print(f'Original: "{sample}"')
        print(f'Reversed : "{reversed_result}"\n')