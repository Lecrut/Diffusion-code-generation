def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

if __name__ == '__main__':
    sample_string = "hello"
    reversed_string = reverse_string_recursive(sample_string)
    print(reversed_string)