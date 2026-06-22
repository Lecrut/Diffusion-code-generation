def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        first_char = s[0]
        rest_of_string = s[1:]
        reversed_rest = reverse_string_recursive(rest_of_string)
        return reversed_rest + first_char

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_string = "world"
    result_recursive = reverse_string_recursive(sample_string)
    result_slicing = reverse_string_slicing(sample_string)
    print("Reversed by recursion:", result_recursive)
    print("Reversed by slicing:", result_slicing)