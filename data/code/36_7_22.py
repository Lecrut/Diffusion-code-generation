def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

def reverse_string_slicing(s):
    return s[::-1]
if __name__ == '__main__':
    sample_string = 'hello'
    reversed_recursive = reverse_string_recursive(sample_string)
    print('Reversed using recursion:', reversed_recursive)
    reversed_slicing = reverse_string_slicing(sample_string)
    print('Reversed using slicing:', reversed_slicing)