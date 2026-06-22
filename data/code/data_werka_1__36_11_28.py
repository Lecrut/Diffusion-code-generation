def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_string = "hello world"
    reversed_string = reverse_string(sample_string)
    print(f"Original: {sample_string}, Reversed: {reversed_string}")