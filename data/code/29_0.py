import sys
def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    input_string_1 = "hello"
    output_1 = reverse_string(input_string_1)
    print(f"Input: {input_string_1}, Output: {output_1}")
    input_string_2 = "Python"
    output_2 = reverse_string(input_string_2)
    print(f"Input: {input_string_2}, Output: {output_2}")
    input_string_3 = ""
    output_3 = reverse_string(input_string_3)
    print(f"Input: {input_string_3}, Output: {output_3}")
    input_string_4 = "12345"
    output_4 = reverse_string(input_string_4)
    print(f"Input: {input_string_4}, Output: {output_4}")
    input_string_5 = "aBcDeFg"
    output_5 = reverse_string(input_string_5)
    print(f"Input: {input_string_5}, Output: {output_5}")