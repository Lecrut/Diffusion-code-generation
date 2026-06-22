def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def reverse_word(s):
    validate_input(s)
    return ''.join([s[i] for i in range(len(s) - 1, -1, -1)])

if __name__ == '__main__':
    sample_input = "test"
    try:
        reversed_output = reverse_word(sample_input)
        print(reversed_output)
    except ValueError as e:
        print(e)