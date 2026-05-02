import sys
def reverse_string(input_string):
    return input_string[::-1]
if __name__ == '__main__':
    sample_input = "hello world"
    reversed_result = reverse_string(sample_input)
    print(reversed_result)