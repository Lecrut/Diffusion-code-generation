def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    return input_string[::-1]

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    reversed_output = reverse_string(sample_input)
    print(reversed_output)