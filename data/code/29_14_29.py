def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_string = "hello"
    reversed_result = reverse_string(sample_string)
    print(reversed_result)