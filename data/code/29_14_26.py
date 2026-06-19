def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_value = "hello"
    reversed_result = reverse_string(sample_value)
    print(reversed_result)