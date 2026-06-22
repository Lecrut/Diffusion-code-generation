def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    input_str = "world"
    result = reverse_string(input_str)
    print(result)