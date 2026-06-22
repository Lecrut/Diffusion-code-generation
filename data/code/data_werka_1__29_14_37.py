def reverse_string(s):
    return ''.join(reversed(s))

if __name__ == '__main__':
    SAMPLE_TEXT = "Alibaba Cloud"
    REVERSED_TEXT = reverse_string(SAMPLE_TEXT)
    print(REVERSED_TEXT)