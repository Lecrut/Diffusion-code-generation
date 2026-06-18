def analyze_string(s: str) -> tuple[set[str], list[str]]:
    """
    Takes a string and returns a tuple containing:
        - A set of unique characters in the string (all occurrences included).
        - A list of characters that appear more than once, sorted alphabetically.

    Args:
        s (str): The input string to analyze.

    Returns:
        tuple[set[str], list[str]]: Tuple with (unique_chars_set, repeated_chars_list)
    """
    char_count = {}
    
    # Count frequency of each character
    for char in s:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    unique_chars = set(char_count.keys())
    repeated_chars = [char for char, count in char_count.items() if count > 1]
    
    # Sort the repeated characters list alphabetically (case-sensitive)
    repeated_chars.sort(key=lambda x: ord(x))
    
    return unique_chars, repeated_chars

if __name__ == '__main__':
    sample_string = "Programming is fun!"
    result_set, result_list = analyze_string(sample_string)

    print(f"Unique characters (set): {result_set}")
    print(f"Repeated characters (list): {result_list}")