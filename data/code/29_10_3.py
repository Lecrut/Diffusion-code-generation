import sys
def reverse_string(input_str):
    return input_str[::-1]
if __name__ == '__main__':
    sample_input_1 = "hello world"
    sample_input_2 = "Python"
    sample_input_3 = ""
    sample_input_4 = "12345"
    print(f"Input: '{sample_input_1}'")
    print(f"Reversed: '{reverse_string(sample_input_1)}'")
    print("-" * 20)
    print(f"Input: '{sample_input_2}'")
    print(f"Reversed: '{reverse_string(sample_input_2)}'")
    print("-" * 20)
    print(f"Input: '{sample_input_3}'")
    print(f"Reversed: '{reverse_string(sample_input_3)}'")
    print("-" * 20)
    print(f"Input: '{sample_input_4}'")
    print(f"Reversed: '{reverse_string(sample_input_4)}'")
    print("-" * 20)