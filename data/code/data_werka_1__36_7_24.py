def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    return s[::-1]

if __name__ == '__main__':
    sample_string = "hello"
    print("Recursive Reverse:", reverse_string_recursive(sample_string))
    print("Slicing Reverse:", reverse_string_slicing(sample_string))