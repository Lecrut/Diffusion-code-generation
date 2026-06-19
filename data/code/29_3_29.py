REVERSE_DIRECTION = -1

def reverse_string(s):
    return s[::REVERSE_DIRECTION]

if __name__ == '__main__':
    sample_input = "Alibaba Cloud"
    result = reverse_string(sample_input)
    print(f"Original: {sample_input}")
    print(f"Reversed: {result}")