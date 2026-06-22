def reverse_string(input_string):
    return input_string[::-1]

if __name__ == '__main__':
    sample_values = [
        "",
        "hello",
        "world",
        "12345",
        "!@#$%",
        "aAaAaA",
        "Python3.8"
    ]
    
    for value in sample_values:
        print(reverse_string(value))