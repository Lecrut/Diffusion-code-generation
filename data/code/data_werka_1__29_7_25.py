def reverse_string(s):
    if isinstance(s, str):
        return s[::-1]
    else:
        raise TypeError("Input must be a string")

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "Python",
        "12345",
        "!@#$%",
        ""
    ]
    
    for value in sample_values:
        try:
            reversed_value = reverse_string(value)
            print(reversed_value)
        except TypeError as e:
            print(e)