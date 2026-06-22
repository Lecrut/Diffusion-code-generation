def reverse_string_recursive(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return s[::-1]

if __name__ == '__main__':
    sample_string = "world"
    try:
        reversed_by_recursion = reverse_string_recursive(sample_string)
        print("Reversed by recursion:", reversed_by_recursion)
    except ValueError as e:
        print(e)

    try:
        reversed_by_slicing = reverse_string_slicing(sample_string)
        print("Reversed by slicing:", reversed_by_slicing)
    except ValueError as e:
        print(e)