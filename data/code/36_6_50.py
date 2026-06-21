def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        first_char = s[0]
        remaining_substring = s[1:]
        reversed_remaining = reverse_string_recursive(remaining_substring)
        return reversed_remaining + first_char

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_string = "example"
    reversed_by_recursion = reverse_string_recursive(sample_string)
    reversed_by_slicing = reverse_string_slicing(sample_string)
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)