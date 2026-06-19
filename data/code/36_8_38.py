def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    original_text = "Python 3.9 🚀"
    reversed_text = reverse_string(original_text)
    print(reversed_text)