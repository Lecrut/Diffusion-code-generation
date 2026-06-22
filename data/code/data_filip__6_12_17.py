SPACE_REPLACEMENT_MAP = {" ": "_"}

def transform_string(input_text):
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string")
    return input_text.replace(" ", "_")

if __name__ == '__main__':
    test_string = "robust python script example"
    transformed = transform_string(test_string)
    print(transformed)