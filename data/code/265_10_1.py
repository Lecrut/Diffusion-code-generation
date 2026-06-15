import re
def extract_alphanumeric(input_string):
    return re.sub(r'[^a-zA-Z0-9]', '', input_string)
if __name__ == '__main__':
    sample_string = "Hello World! 123 Python is fun, isn't it?"
    result = extract_alphanumeric(sample_string)
    print(result)