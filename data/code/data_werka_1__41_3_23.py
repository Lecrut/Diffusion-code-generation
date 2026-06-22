def process_string(input_str):
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string")
    
    lowercase_str = input_str.lower()
    reversed_case_str = ''.join(c.swapcase() for c in input_str)
    return (input_str, lowercase_str, reversed_case_str)

if __name__ == '__main__':
    sample = "Hello World"
    try:
        result = process_string(sample)
        print(result)
    except ValueError as e:
        print(e)