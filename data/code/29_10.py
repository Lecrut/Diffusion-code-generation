import sys
def reverse_string(input_str):
    return input_str[::-1]
if __name__ == '__main__':
    sample_input_1 = "hello world"
    sample_input_2 = "Python"
    sample_input_3 = ""
    sample_input_4 = "12345"
    print(f"Input 1: {sample_input_1}")
    print(f"Reversed 1: {reverse_string(sample_input_1)}\n")
    print(f"Input 2: {sample_input_2}")
    print(f"Reversed 2: {reverse_string(sample_input_2)}\n")
    print(f"Input 3: {sample_input_3}")
    print(f"Reversed 3: {reverse_string(sample_input_3)}\n")
    print(f"Input 4: {sample_input_4}")
    print(f"Reversed 4: {reverse_string(sample_input_4)}\n")