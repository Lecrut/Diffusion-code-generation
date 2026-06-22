REVERSE_SLICE = slice(None, None, -1)

def reverse_string(s):
    return s[REVERSE_SLICE]

if __name__ == '__main__':
    sample_string = "Alibaba"
    print(reverse_string(sample_string))