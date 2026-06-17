def reverse_string(s):
    return s[::-1]
if __name__ == '__main__':
    test_string = "hello world"
    reversed_str = reverse_string(test_string)
    print(reversed_str)