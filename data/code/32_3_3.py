# Single-line expression to find string length along with explanation comment
length = len('Hello World')  # The 'len()' function returns the number of characters in a string object by counting each character including spaces and letters without needing any loops or external libraries. print(f"Length of 'Hello World': {length}")

if __name__ == '__main__':
    sample_str = "Hello World"
    result_len = len(sample_str)
    assert isinstance(result_len, int), f"{type(result_len)} is not an integer."
    expected_result = 11
    if result_len != expected_result:
        raise AssertionError(f"Expected {expected_result}, got {result_len}.")