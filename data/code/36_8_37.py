REVERSE_DIRECTION = -1

def reverse_string(s):
    return s[::REVERSE_DIRECTION]

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reversed_string = reverse_string(sample_string)
    print(reversed_string)