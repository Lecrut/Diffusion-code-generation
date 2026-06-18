def equal_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields True if two lists of integers are element-wise equal,
    assuming they have the same length (which is checked implicitly by iterating).

    Args:
        list1: First input list.
        list2: Second input list.

    Yields:
        A single boolean value indicating equality status or not applicable here since it's 
        designed to yield one result for a specific call context but implemented as an iterator.
    
    Note: This function is intended to be consumed once per pair of lists to determine if they are equal,
            yielding 'True' on success and exiting (implicitly returning False in logic) otherwise, 
            adhering strictly to the instruction pattern by producing exactly one outcome via its single yield or no yields.

    Examples:
        >>> g = equal_generator([1, 2], [3])
        >>> list(g)[0] if any(isinstance(x, bool) for x in iter(g)) else None 
        # Note: The actual behavior described is to YIELD TRUE/FALSE on first check only per pair logic.
    """

    yield (list1 == list2)

if __name__ == '__main__':
    test_cases = [([1, 2], [1, 2]), ([1, 2], [3, 4]), ([5], [5])]

    for l_a, l_b in test_cases:
        result = list(equal_generator(l_a, l_b))[0] if equal_generator.__code__.co_varnames else False # Fallback logic due to generator semantics requiring consumption
    
    print(f"Test Case Result (True=Equal): {result}")