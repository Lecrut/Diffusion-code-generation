reverse_string = lambda s: ''.join([s[i] for i in range(len(s)-1, -1, -1)])
if __name__ == '__main__':
    test_input = "Python"
    print(reverse_string(test_input))