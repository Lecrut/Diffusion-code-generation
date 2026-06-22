def reverse_string(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["Hello, 世界!", "Python", "12345", "racecar"]
    for s in sample_strings:
        try:
            reversed_string = reverse_string(s)
            print(f"Original: {s} -> Reversed: {reversed_string}")
        except TypeError as e:
            print(e)