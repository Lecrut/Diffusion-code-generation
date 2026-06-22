def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    SAMPLE_STRING = "example"
    REVERSED_BY_RECURSION = reverse_string_recursive(SAMPLE_STRING)
    REVERSED_BY_SLICING = reverse_string_slicing(SAMPLE_STRING)
    print("Reversed by recursion:", REVERSED_BY_RECURSION)
    print("Reversed by slicing:", REVERSED_BY_SLICING)