def reverse_string_recursive(s):
    def validate_input(input_str):
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
    
    validate_input(s)
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    def validate_input(input_str):
        if not isinstance(input_str, str):
            raise ValueError("Input must be a string")
    
    validate_input(s)
    return s[::-1]

if __name__ == '__main__':
    sample_string = "example"
    reversed_by_recursion = reverse_string_recursive(sample_string)
    reversed_by_slicing = reverse_string_slicing(sample_string)
    print("Reversed by recursion:", reversed_by_recursion)
    print("Reversed by slicing:", reversed_by_slicing)