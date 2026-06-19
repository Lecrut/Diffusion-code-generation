def reverse_string(s):
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)
    return ''.join(reversed_chars)

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    result = reverse_string(sample_input)
    print(f"Original: {sample_input}")
    print(f"Reversed: {result}")