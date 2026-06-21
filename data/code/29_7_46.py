def reverse_word(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_input = "test"
    try:
        reversed_output = reverse_word(sample_input)
        print(reversed_output)
    except ValueError as e:
        print(e)