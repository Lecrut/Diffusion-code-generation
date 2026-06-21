reverse_string = lambda s: ''.join(chr(i) for i in range(ord(s[-1]), ord(s[0]) - 1, -1)) if s else ''
if __name__ == '__main__':
    test_input = "Alibaba"
    reversed_output = reverse_string(test_input)
    print(reversed_output)