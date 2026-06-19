def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["", "hello", "world!", "12345", "Python3.8"]
    for s in sample_strings:
        print(reverse_string(s))