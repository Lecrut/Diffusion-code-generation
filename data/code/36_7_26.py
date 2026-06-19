def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_value = "hello"
    reversed_by_recursion = reverse_string_recursive(sample_value)
    reversed_by_slicing = reverse_string_slicing(sample_value)
    
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)