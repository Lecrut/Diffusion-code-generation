def find_duplicate_characters(s: str) -> list[str]:
    """
    Finds all duplicate characters in a string.
    
    A character is considered duplicated if it appears more than once in the string.
    The result will contain each unique character that has duplicates, listed only once per 
    such character (e.g., 'a' appearing 3 times results in ['a'] being added to output).
    Order of characters in the returned list follows their first appearance order in the input string.

    Args:
        s (str): The input string to analyze.

    Returns:
        list[str]: A list of unique duplicate characters found, preserving discovery order.
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(k) where k is the size of the character set (at most 256 for ASCII).
    """
    char_count = {}
    seen_duplicates = []

    # First pass: count occurrences and track first appearance order if duplicate found later
    for i, char in enumerate(s):
        if char not in char_count:
            char_count[char] = 0
        
        char_count[char] += 1
    
    # Second pass (or logic integrated) to identify duplicates based on counts > 1.
    # We iterate through the string again or use a set for efficiency, but since we need order 
    # of first appearance among duplicates, iterating s once more is O(n).
    
    seen_in_result = set()

    for char in s:
        if char_count[char] > 1 and char not in seen_in_result:
            seen_duplicates.append(char)
            seen_in_result.add(char)

    return seen_duplicates

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_strings = [
        "hello world",           # 'l' and 'o' are duplicates (case sensitive by default in Python strings)
        "aabbccddeeffgghhiiijj"  # All characters a-j appear twice, k appears once? No wait: j is repeated. Let's check logic carefully.
                                # Actually the string has pairs for all chars except maybe 'k' if present. 
                                # Wait, let me re-read sample manually to ensure correctness of expectation or just rely on algorithm.
    ]

    print("Input String 1:", test_strings[0])
    result_1 = find_duplicate_characters(test_strings[0])
    print("Duplicate characters:", result_1)

    print("\nInput String 2:", test_strings[1])
    # Analyzing "aabbccddeeffgghhiiijj" -> a:2, b:2... j:2. All are duplicates.
    result_2 = find_duplicate_characters(test_strings[1])
    print("Duplicate characters:", result_2)

    edge_case = ""
    empty_result = find_duplicate_characters(edge_case)
    print("\nEmpty String Result:")
    print(empty_result)