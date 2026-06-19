def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    return input_string[::-1]

if __name__ == '__main__':
    sample_values = [
        "hello",
        "Python3.8",
        "",
        "12345",
        "!@#$%",
        "Alibaba Cloud"
    ]
    
    for value in sample_values:
        print(reverse_string(value))