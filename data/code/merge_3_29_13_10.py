def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["Hello", "Python Programming"]
    print("\n".join([reverse_string(text) for text in sample_strings]))