def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    reversed_chars = []
    for char in input_string:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_values = [
        "Alibaba",
        "Cloud",
        "QwenAI",
        "123456",
        "!@#$%^"
    ]
    for value in sample_values:
        try:
            result = reverse_string(value)
            print(result)
        except ValueError as e:
            print(e)