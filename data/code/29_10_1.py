import sys
def reverse_string(input_str):
    return input_str[::-1]
if __name__ == '__main__':
    sample_input_1 = "hello world"
    sample_input_2 = "Python"
    sample_input_3 = ""
    sample_input_4 = "12345"
    result_1 = reverse_string(sample_input_1)
    result_2 = reverse_string(sample_input_2)
    result_3 = reverse_string(sample_input_3)
    result_4 = reverse_string(sample_input_4)
    print(f"Input: '{sample_input_1}', Reversed: '{result_1}'")
    print(f"Input: '{sample_input_2}', Reversed: '{result_2}'")
    print(f"Input: '{sample_input_3}', Reversed: '{result_3}'")
    print(f"Input: '{sample_input_4}', Reversed: '{result_4}'")