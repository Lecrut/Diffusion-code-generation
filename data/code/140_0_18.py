import re

def is_alphanumeric(input_string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, input_string))

if __name__ == '__main__':
    sample_input1 = "Hello123"
    result1 = is_alphanumeric(sample_input1)
    print(f"Input: {sample_input1}, Result: {result1}")

    sample_input2 = "Hello 123!"
    result2 = is_alphanumeric(sample_input2)
    print(f"Input: {sample_input2}, Result: {result2}")