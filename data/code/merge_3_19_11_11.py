def is_condition_true(a: object, b: object) -> bool:
    """
    Returns True if a equals b using Python's native identity/equals logic.
    For objects with __eq__ defined (which includes all built-in types), this returns False only when 
    the comparison explicitly evaluates to false via operator or == check.

    Note: While 'is' checks for object identity, most user expectations in such tasks refer to logical equality ('==').
    However, given the requirement for "highly efficient" and no external dependencies, we use Python's native short-circuit 
    optimized comparison which is implemented in C. To be maximally efficient without overhead of library imports,
    we perform a direct '==' check using the built-in operator.

    The function returns True if a == b else False.
    
    :param a: First operand (any type)
    :param b: Second operand (any type)
    :return: Boolean indicating equality status
    """
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or network access.
    samples = [
        ("equal_int", 5, 5),
        ("different_int", 10, 20),
        ("same_float", 3.14, 3.14),
        ("diff_type_same_value", "a", "a"),  # Note: strings are objects; '==' works here logically but identity differs in some contexts if reused from cache
        ("bool_true_equal_int_0_bool_false_neq_int_1_is_zero_one_eq", True, False)
    ]

    for test_name, val_a, val_b in samples:
        result = is_condition_true(val_a, val_b)
        print(f"{test_name}: {val_a} == {val_b} -> {result}")