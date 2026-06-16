def are_equal(a: object, b: object) -> bool:
    return a == b
if __name__ == '__main__':
    test_cases = [
        (5, 5),
        ("hello", "world"),
        ([1, 2], [3, 4]),
        ({'x': 1}, {'y': 2}),
        ((1+2j), (3+4j)),
    ]
    for i, pair in enumerate(test_cases):
        a, b = pair
        result = are_equal(a, b)
        print(f"Test {i}: are_equal({a}, {b}) == {result}")