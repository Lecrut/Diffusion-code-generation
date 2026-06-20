def is_palindrome_symmetric(sequence):
    return all(a == b for a, b in zip(sequence, reversed(sequence)))

if __name__ == '__main__':
    test_values = [
        [1, 2, 3, 2, 1],
        [1, 2, 3, 4, 5],
        "racecar",
        "hello",
        [7],
        []
    ]

    for value in test_values:
        result = is_palindrome_symmetric(value)
        print(f"{value}: {result}")