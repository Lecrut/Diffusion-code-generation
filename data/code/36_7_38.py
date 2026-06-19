def reverse_string_recursive(s):
    if not s:
        return ""
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    test_string = "world"
    reversed_with_recursion = reverse_string_recursive(test_string)
    reversed_with_slicing = reverse_string_slicing(test_string)
    print("Reversed using recursion:", reversed_with_recursion)
    print("Reversed using slicing:", reversed_with_slicing)