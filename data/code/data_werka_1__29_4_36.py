def reverse_string_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == '__main__':
    sample_string = "hello"
    result = reverse_string_iterative(sample_string)
    print(result)