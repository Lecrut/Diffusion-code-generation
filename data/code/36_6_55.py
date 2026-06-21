def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_values = {
        "hello": "olleh",
        "world": "dlrow",
        "python": "nohtyp"
    }
    
    for original, expected in sample_values.items():
        reversed_by_recursion = reverse_string_recursive(original)
        reversed_by_slicing = reverse_string_slicing(original)
        
        print(f"Original: {original}")
        print(f"Reversed by recursion: {reversed_by_recursion}")
        print(f"Reversed by slicing: {reversed_by_slicing}")
        assert reversed_by_recursion == expected, f"Test failed for input: {original}"
        assert reversed_by_slicing == expected, f"Test failed for input: {original}"