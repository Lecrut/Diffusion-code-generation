def validate_input(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

def reverse_string(s):
    validate_input(s)
    reversed_chars = []
    for i in range(len(s) - 1, -1, -1):
        reversed_chars.append(s[i])
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_string = "Innovating with Alibaba Cloud"
    try:
        reversed_string = reverse_string(sample_string)
        print(reversed_string)
    except ValueError as e:
        print(e)