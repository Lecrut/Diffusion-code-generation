def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]
if __name__ == '__main__':
    sample_string = 'hello'
    reversed_string_recursive = reverse_string_recursive(sample_string)
    print(reversed_string_recursive)
    reversed_string_slicing = sample_string[::-1]
    print(reversed_string_slicing)