def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    sample_string = "hello world"
    reversed_string = reverse_string(sample_string)
    print(f"Original: {sample_string}, Reversed: {reversed_string}")