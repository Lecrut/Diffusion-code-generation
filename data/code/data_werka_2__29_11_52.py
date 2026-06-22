def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    SAMPLE_STRINGS = [
        "Hello, World!",
        "Alibaba Cloud",
        "Python Programming"
    ]
    
    for original in SAMPLE_STRINGS:
        try:
            reversed_string = reverse_string(original)
            print(f"Original: {original}, Reversed: {reversed_string}")
        except ValueError as e:
            print(e)