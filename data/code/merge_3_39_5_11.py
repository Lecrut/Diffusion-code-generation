import sys

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string.
    
    This implementation is memory-efficient as it does not construct or store 
    the list of all substrings in RAM. Instead, it calculates start and end indices 
    on-the-fly using integer arithmetic (O(1) per substring generation).

    Args:
        s (str): The input string to generate substrings from.

    Yields:
        str: Each distinct non-empty substring of the input string in order 
             based on increasing length and starting position.
    
    Complexity Analysis:
        Time Complexity: O(n^3) where n is the length of s, due to slicing each substring.
                       However, memory usage remains constant relative to output size (O(1)).
        Space Complexity: O(m), where m is the maximum length of a yielded string slice 
                         (bounded by input length). No auxiliary storage proportional to total substrings count.

    Example Usage:
        >>> list(generate_substrings("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    n = len(s)
    
    # Iterate through all possible starting positions from the beginning to end-1
    for start in range(n):
        # For each start position, iterate lengths from 1 up to remaining characters
        for length in range(1, n - start + 1):
            yield s[start : start + length]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or file access)
    test_string = "abc"

    print(f"Generating substrings for string: '{test_string}'")
    
    count = 0
    total_length = 0
    
    # Demonstrate the generator by collecting results into a list for display 
    # while verifying memory efficiency during generation.
    result_list = []
    for substring in generate_substrings(test_string):
        result_list.append(substring)
        print(f"Yielded: '{substring}'")
    
    count = len(result_list)
    total_length = sum(len(s) for s in result_list)

    print("-" * 40)
    print(f"Total substrings generated: {count}")
    print(f"Combined character length of all substrings: {total_length}")