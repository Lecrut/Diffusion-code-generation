def to_uppercase_safe(input_value):
    if isinstance(input_value, str):
        return input_value.upper()
    else:
        raise TypeError("Input must be a string")
if __name__ == '__main__':
    sample1 = "hello world"
    sample2 = "PYTHON"
    sample3 = 12345
    sample4 = None
    print(f"'{sample1}' -> {to_uppercase_safe(sample1)}")
    print(f"'{sample2}' -> {to_uppercase_safe(sample2)}")
    try:
        to_uppercase_safe(sample3)
    except TypeError as e:
        print(f"Attempting to process {sample3}: Error caught - {e}")
    try:
        to_uppercase_safe(sample4)
    except TypeError as e:
        print(f"Attempting to process {sample4}: Error caught - {e}")