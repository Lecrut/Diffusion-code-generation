def reverse_string(text):
    """Reverses a given string in-place using slicing."""
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to avoid any user input or external dependencies
    test_strings = [
        "Hello, World!",
        "Python 3.9",
        "",
        "!_-_a"
    ]

    for s in test_strings:
        reversed_s = reverse_string(s)
        print(reversed_s)