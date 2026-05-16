def reverse_string_iterative(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
if __name__ == '__main__':
    sample_string = "hello"
    reversed_result = reverse_string_iterative(sample_string)
    print(reversed_result)
    sample_string_2 = "world"
    reversed_result_2 = reverse_string_iterative(sample_string_2)
    print(reversed_result_2)
    sample_string_3 = "python"
    reversed_result_3 = reverse_string_iterative(sample_string_3)
    print(reversed_result_3)