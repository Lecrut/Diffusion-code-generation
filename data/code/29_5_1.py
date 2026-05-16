def reverse_string_iterative(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
if __name__ == '__main__':
    sample_string = "hello"
    reversed_result = reverse_string_iterative(sample_string)
    print(reversed_result)