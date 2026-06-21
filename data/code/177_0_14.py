def split_string_by_spaces(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    return s.split()

if __name__ == '__main__':
    sample = "Hello World This Is A Test"
    print(split_string_by_spaces(sample))