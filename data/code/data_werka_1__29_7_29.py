def reverse_string(input_string):
    if isinstance(input_string, str):
        return input_string[::-1]
    else:
        raise ValueError("Input must be a string")

if __name__ == '__main__':
    sample_values = ["hello", "world", 12345, "Python"]
    for value in sample_values:
        try:
            print(reverse_string(value))
        except ValueError as e:
            print(e)