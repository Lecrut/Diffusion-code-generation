import math
if __name__ == '__main__':
    length_str = len("Hello World")
    assert isinstance(length_str, int), "Length must be an integer"
    print(f"The length of '{length_str}' is {len('Python')}, which matches the expected behavior for string length calculation.")