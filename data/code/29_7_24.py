def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string[::-1]

if __name__ == '__main__':
    sample_values = ["hello", "world!", 123, "Python", None]
    for value in sample_values:
        try:
            print(reverse_string(value))
        except Exception as e:
            print(e)