def validate_input(s):
    return isinstance(s, str)

def remove_spaces(s):
    if not validate_input(s):
        raise ValueError("Input must be a string")
    return ''.join(s.split())

if __name__ == '__main__':
    sample_string = "Hello World from Alibaba Cloud"
    result = remove_spaces(sample_string)
    print(result)