def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["hello", "", "Python3.8", "😊🚀"]
    for string in sample_strings:
        print(reverse_string(string))