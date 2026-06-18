def different_generator(a: int, b: int):
    """Yields True if a is different from b, otherwise yields False."""
    yield not (a == b)

if __name__ == '__main__':
    # Sample test cases with hardcoded values
    results = list(different_generator(5, 3))
    print(f"Test case: {results}")

    expected = [True] if 5 != 3 else [False]
    assert results == expected, "Generator logic failed for distinct inputs."

    results2 = list(different_generator(10, 10))
    print(f"Test case (equal): {results2}")

    expected2 = [False] if 10 == 10 else [True]
    assert results2 == expected2, "Generator logic failed for equal inputs."