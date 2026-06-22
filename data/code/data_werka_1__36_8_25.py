def is_valid_string(s):
    return isinstance(s, str)

def reverse_string(s):
    if not is_valid_string(s):
        raise ValueError("Input must be a string")
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)