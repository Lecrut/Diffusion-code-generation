def analyze_string_chars(text: str) -> tuple[set[str], list[str]]:
    """
    Analyzes a string to return unique characters and repeated characters.

    Args:
        text (str): The input string to analyze.

    Returns:
        tuple: A tuple containing two elements:
            - set(str): A set of all unique characters present in the string.
            - list[str]: A list of characters that appear more than once, 
                         preserving their first occurrence order.
    
    Note:
        This function is case-sensitive and includes spaces and punctuation if present.
    """
    char_count = {}
    seen_order = []  # To maintain the order of first appearance for uniqueness check logic later
    
    # First pass: Count character frequencies and track unique characters in order
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    unique_chars_set = set()
    
    # Second pass to build the list of repeated chars preserving first appearance order 
    # while also building the full unique set (though set is commutative).
    for char in text:
        if char not in seen_order and char_count[char] > 1:
            seen_order.append(char)

    return (unique_chars_set, seen_order)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input or external files used.
    sample_input = "hello world!"
    
    unique_chars, repeated_chars = analyze_string_chars(sample_input)
    
    print(f"Input: '{sample_input}'")
    print(f"Unique characters set: {unique_chars}")
    print(f"Repeated characters list (first occurrence order): {repeated_chars}")