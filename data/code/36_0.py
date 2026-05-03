import sys
def reverse_string(input_string):
    return input_string[::-1]
if __name__ == '__main__':
    sample_string = "hello world"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)