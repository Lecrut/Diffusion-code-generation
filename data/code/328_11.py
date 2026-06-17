import sys
def calculate_string_length(input_value):
    try:
        return len(input_value)
    except TypeError:
        return "Error: Input must be a string."
if __name__ == '__main__':
    sample_inputs = [
        "hello world",
        "Python",
        12345,
        None,
        ["list"]
    ]
    for sample in sample_inputs:
        result = calculate_string_length(sample)
        print(f"Input: {repr(sample)}, Length: {result}")