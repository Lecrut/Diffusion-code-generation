def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    sample_values = [
        "hello",
        12345,
        [1, 2, 3],
        {"key": "value"},
        None,
        True,
        False
    ]
    
    for value in sample_values:
        try:
            result = reverse_string(str(value))
            print(result)
        except Exception as e:
            print(e)