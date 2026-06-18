import itertools

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    This implementation is memory-efficient as it does not store all substrings in memory;
    instead, it generates them one by one using nested loops and the yield statement.

    Args:
        s (str): The input string from which to generate substrings.

    Yields:
        str: Each substring of s, starting with single characters up to the full string itself.
             Substrings are yielded in order of their start index, then end index.
    
    Example:
        >>> list(generate_substrings("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    length = len(s)
    for i in range(length):  # Start index of the substring
        for j in range(i + 1, length + 1):  # End index (exclusive) of the substring
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "programming"
    
    print(f"All substrings of '{sample_string}':")
    for sub in generate_substrings(sample_string):
        print(sub)

    # Additional test with a shorter string to verify correctness quickly
    short_sample = "abc"
    print(f"\nAll substrings of '{short_sample}':")
    count = 0
    for sub in generate_substrings(short_sample):
        count += 1
    print(f"Total number of substrings: {count}")

    # Verify against expected output manually calculated
    manual_expected = ['a', 'ab', 'abc', 'b', 'bc', 'c']
    result_list = list(generate_substrings(short_sample))
    
    if result_list == manual_expected:
        print("Test passed!")
    else:
        print(f"Test failed. Expected {manual_expected}, got {result_list}")