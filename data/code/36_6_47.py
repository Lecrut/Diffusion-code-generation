def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    else:
        mid = len(s) // 2
        left_reversed = reverse_string_recursive(s[:mid])
        right_reversed = reverse_string_recursive(s[mid:])
        return right_reversed + left_reversed

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_string = "example"
    reversed_by_recursion = reverse_string_recursive(sample_string)
    reversed_by_slicing = reverse_string_slicing(sample_string)
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)