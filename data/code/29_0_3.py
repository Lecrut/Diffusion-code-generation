import sys
def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    input_string_1 = "hello"
    reversed_1 = reverse_string(input_string_1)
    print(reversed_1)
    input_string_2 = "Python"
    reversed_2 = reverse_string(input_string_2)
    print(reversed_2)
    input_string_3 = ""
    reversed_3 = reverse_string(input_string_3)
    print(reversed_3)
    input_string_4 = "12345!@#"
    reversed_4 = reverse_string(input_string_4)
    print(reversed_4)