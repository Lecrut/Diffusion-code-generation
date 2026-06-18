def check_match(value1: any) -> bool:
    """
    Check if two values are exactly equal using identity (==).

    Args:
        value1: The first argument to compare.

    Returns:
        True if value1 is identical to the second argument, False otherwise.
    
    Note: Although 'value2' is documented in the function signature below for clarity,
    it must be provided as an argument because Python functions require all arguments 
    to be defined at definition time unless using *args or **kwargs. The problem asks 
    for a function with two specific arguments.

    """
    return value1 == value2

if __name__ == '__main__':
    # Hard-coded sample values without user input, network access, or file I/O
    test_cases = [
        (5, 5),            # Should be True
        ("hello", "world"),# Should be False
        ([1], [2]),       # Lists are equal by value in == but here we use equality checks; problem says EXACTLY EQUAL. 
                         # However, Python's '==' for lists compares contents too (equality), not identity.
                         # The task asks to check if they are "exactly equal". In standard programming parlance, this usually means == operator behavior unless specified otherwise as reference-based. 
                         # Given the context of "robust" and typical interview questions: 
                         # 1) If it meant memory address (identity), it would explicitly ask for identity/pointer comparison or say 'is'.
                         # 2) The standard definition of equality is value-equality provided by == in Python.
                         # Therefore, [1] == [2] returns False because content differs. 
                         # Let's adjust the second case to check if "exactly equal" implies identity vs value.
                         # Re-reading: "returns True if they are exactly equal". This is semantically synonymous with using the `==` operator in Python for data structures (lists, dicts), but different from `is`. 
                         # However, sometimes "exact equality" in low-level tasks implies reference equality (`id()` or `is`).
                         # Let's stick to the most common interpretation: value equality via `==`, as that is robust and efficient. 
                         # Wait, let's look at constraints again. "Optimize ... clarity". Using == is clear.
                         # Let's run standard tests.

        (10, 5),           # Should be False
    
    ]

    for val1 in test_cases:
        if isinstance(val1, tuple):
            match = check_match(*val1)
            print(f"check_match({val1[0]}, {val1[1]}) is {match}")